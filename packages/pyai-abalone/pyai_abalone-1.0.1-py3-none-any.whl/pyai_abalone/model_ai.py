# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:38:30 2022

@author: hlocke
"""

from .constants import AI_WEIGHTS
import tensorflow as tf
from tensorflow.keras import Model, Input
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.python.keras.engine import data_adapter


class ResidualBlock(layers.Layer):
    """
    residual layer with Conv2D layers as it is usually used in image
    recoginition
    
    Args:
        filters: int, number of filters for the Conv2D layers
    """
    def __init__(self, filters: int, **kwargs):
        super(ResidualBlock, self).__init__(**kwargs)
        self.filters = filters

        self.conv1 = layers.Conv2D(filters, 3, padding="same")
        self.norm1 = layers.BatchNormalization(axis=1)
        self.act1 = layers.Activation("relu")

        self.conv2 = layers.Conv2D(filters, 3, padding="same")
        self.norm2 = layers.BatchNormalization(axis=1)
        self.add2 = layers.Add()
        self.act2 = layers.Activation("relu")

    def call(self, x, training=False):
        out = self.conv1(x, training=training)
        out = self.norm1(out, training=training)
        out = self.act1(out, training=training)
        out = self.conv2(out, training=training)
        out = self.norm2(out, training=training)
        out = self.add2([out, x])
        out = self.act2(out, training=training)
        return out

    def get_config(self):
        config = {
            'filters': self.filters,
            }
        base_config = super(ResidualBlock, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))


def build_magister_zero(num_resblocks, filters, num_actions):
    params = locals()
    x_inp = Input(
        (11, 11, 4),
        dtype=tf.float32
    )

    x = layers.Conv2D(filters, 3, padding="same", name="ludi_input")(x_inp)
    x = layers.BatchNormalization(axis=1)(x)
    x = layers.Activation("relu")(x)
    for _ in range(num_resblocks):
        x = ResidualBlock(filters)(x)

    pol_out = layers.Conv2D(filters, 3, padding="same")(x)
    pol_out = layers.BatchNormalization(axis=1)(pol_out)
    pol_out = layers.Activation("relu")(pol_out)
    pol_out = layers.Flatten()(pol_out)
    pol_out = layers.Dense(
        num_actions, name="pol_prediction")(pol_out)

    val_out = layers.Conv2D(filters, 3, padding="same")(x)
    val_out = layers.BatchNormalization(axis=1)(val_out)
    val_out = layers.Activation("relu")(val_out)
    val_out = layers.Flatten()(val_out)
    val_out = layers.Dense(2*filters, activation="relu")(val_out)
    val_out = layers.Dense(
        1, activation="tanh", name="val_prediction")(val_out)

    model = Model(x_inp, [pol_out, val_out])
    return model, params


class MagisterZero(Model):
    """
    trainable model for Abalone based on the image recognition model applied
    by AlphaZero
    
    Args:
        num_resblocks: number of residual layers
        filtrs: number of filters for the Conv2D layers within the residual
            layers
        num_actions: number of possible actions used
    """
    def __init__(self, num_resblocks, filters, num_actions):
        super().__init__()

        self.model, self.params = build_magister_zero(
            num_resblocks, filters, num_actions)
        self.mse = losses.MeanSquaredError()
        self.sce = losses.SparseCategoricalCrossentropy(
            from_logits=True,
            reduction=losses.Reduction.NONE
        )

        self.policy_tracker = tf.keras.metrics.Mean(name='policy_loss')
        self.value_tracker = tf.keras.metrics.Mean(name='value_loss')
        self.loss_tracker = tf.keras.metrics.Mean(name='total_loss')
        self.magister_trackers = [
            self.policy_tracker,
            self.value_tracker,
            self.loss_tracker
        ]

    def call(self, x, training=False):
        return self.model(x, training)

    def policy_loss(self, y_true, y_pred, values_true):
        pol_loss = self.sce(y_true, y_pred)
        return tf.reduce_mean(pol_loss * values_true)

    def train_step(self, data):
        data = data_adapter.expand_1d(data)
        x, y, sample_weight = data_adapter.unpack_x_y_sample_weight(data)
        act_real, val_real = y

        with tf.GradientTape() as tape:
            pred = self(x, training=True)
            alogits_pred, val_pred = pred
            val_loss = self.mse(val_real, val_pred)
            pol_loss = self.policy_loss(act_real, alogits_pred, val_real)
            loss = val_loss + pol_loss

        gradients = tape.gradient(loss, self.trainable_variables)
        self.optimizer.apply_gradients(
            zip(gradients, self.trainable_variables))

        self.policy_tracker.update_state(pol_loss)
        self.value_tracker.update_state(val_loss)
        self.loss_tracker.update_state(loss)
        return {t.name: t.result() for t in self.magister_trackers}

    @property
    def metrics(self):
        return self.magister_trackers


def get_trained_magister_zero() -> MagisterZero:
    """
    generates an instance of 'MagisterZero', laods the trained weights and
    returns the model.
    
    Returns:
        trained MagisterZero model
    """
    model = MagisterZero(2, 64, 1506)
    basic_inp = tf.zeros((1, 11, 11, 4))
    _ = model(basic_inp)
    model.load_weights(AI_WEIGHTS)
    return model
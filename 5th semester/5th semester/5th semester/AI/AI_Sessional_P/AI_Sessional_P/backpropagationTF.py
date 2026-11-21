import tensorflow as tf

X = tf.constant([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y = tf.constant([[0.],[1.],[1.],[0.]])

model = tf.keras.Sequential([
    tf.keras.Input(shape=(2,)),
    tf.keras.layers.Dense(2, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='sgd',
    loss='mse'
)

model.fit(X, y, epochs=100, verbose=0)

print(model.predict(X))
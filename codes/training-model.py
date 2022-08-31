# Create early stopping callback
early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss',patience=3)

# Store model history into variable
history = model.fit(train_data,validation_data = valid_data,validation_freq=1,epochs = 50,callbacks = [early_stopping],verbose = 1,)

# Plot model training history
def plot_history():
    plt.plot(history.history['acc'],label='acc')
    plt.plot(history.history['val_acc'],label='val_acc')
    plt.plot(history.history['loss'],label='loss')
    plt.plot(history.history['val_loss'],label='val_loss')
    plt.legend()
    plt.title('Training History')
    plt.xlabel('epoch')
    plt.ylabel('value')
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('output/training_history.jpg')
    plt.show()

plot_history()

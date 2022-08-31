# Processing image files into numpy array
def process_label(label):
    label = [i == unique_label for i in label]
    label = np.array(label).astype(int)
    return label
  
def processImage(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image,channels=3)
    image = tf.image.convert_image_dtype(image,tf.float32)
    image = tf.image.resize(image,size=[224,224])
    return image

# Create Batch data of numpy array
def pairData(image,label):
    return processImage(image),label
  
def batchData(image,label=None,for_valid=False,for_test=False):
    if for_test:
        data = tf.data.Dataset.from_tensor_slices((image))
        batch = data.map(processImage).batch(32)
        return batch
    elif for_valid:
        data = tf.data.Dataset.from_tensor_slices((tf.constant(image),tf.constant(label)))
        batch = data.map(pairData).batch(32)
        return batch
    else:
        data = tf.data.Dataset.from_tensor_slices((tf.constant(image),tf.constant(label)))
        data = data.shuffle(buffer_size=len(image))
        batch = data.map(pairData).batch(32)
        return batch
  
unique_label = np.unique(y_test)
y_test = process_label(y_test)
y_train = process_label(y_train)

train_data = batchData(x_train,y_train)
valid_data = batchData(x_test,y_test,for_valid=True)

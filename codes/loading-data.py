def loading_data():
    dirname = 'dataset/'
    dirtype = ['train/', 'valid/']
    dirclass = ['with_mask/', 'without_mask/']
    
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    
    for typ in dirtype:
        for cls in dirclass:
            for i in os.listdir(dirname+typ+cls):
                if typ == 'train/':
                    x_train.append(dirname+'train/'+cls+i)
                    y_train.append(cls[:-1])
                else:
                    x_test.append(dirname+'valid/'+cls+i)
                    y_test.append(cls[:-1])
    return np.array(x_train),np.array(y_train),np.array(x_test),np.array(y_test)


# Run loading_data() function
x_train,y_train,x_test,y_test = loading_data()

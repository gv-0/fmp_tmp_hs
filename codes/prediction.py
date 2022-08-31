
def predict(unseen_image = []):
    test_data = batchData(unseen_image,for_test=True)
    prediction = model.predict(test_data)

    for image,pred in zip(unseen_image,prediction):
        fig,axes = plt.subplots(nrows=1,ncols=2)
        axes[0].imshow(processImage(image))
        axes[0].axis(False)
        axes[0].set_title('Actual Image')

        axes[1].bar([0,1],pred)
        axes[1].set_xticks([0,1])
        axes[1].set_xticklabels(['with_mask','without_mask'])
        axes[1].set_title('Prediction Probability')
        plt.savefig(f'output/prediction_test_{image.split("/")[-1].split(".")[0]}.jpg')
        plt.show()
                    
predict(list(map(lambda x : f'test/{x}', os.listdir('test'))))

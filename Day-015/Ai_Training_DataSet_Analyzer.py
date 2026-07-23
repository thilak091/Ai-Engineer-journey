import numpy as np

#Section 1: Heading
print('====================================================')
print('             AI TRAINING DATASET ANALYZER')
print('====================================================\n')

#Section 2:Data Set Information
dataset = np.array([
    [5200, 4800, 5000, 5100, 4950],
    [88, 91, 86, 94, 90],
    [120, 140, 110, 150, 130],
    [2.1, 1.8, 2.4, 1.6, 2.0]
])

categories = np.array([
    "Images",
    "Accuracy",
    "Training Time",
    "Loss"
])

models = np.array([
    "CNN",
    "ResNet",
    "MobileNet",
    "EfficientNet",
    "VisionTransformer"
])

print('Data Set Loaded Successfully!\n')

print('Data Set Information\n')

print(f'Total Models: {models.size}')
print(f'Total Metrics: {categories.size}')
print(f'Data set Shape: {dataset.shape}\n')

print('----------------------------------------------------\n')

#Section 3:Training Statistics
print('       Training Statistics\n')

print(f'Average Images: {dataset[0,::].mean():.2f}')
print(f'Average Accuracy: {dataset[1,::].mean():.2f}%')
print(f'Average Training Time: {dataset[2,::].mean():.2f} mins')
print(f'Average Loss: {dataset[3,::].mean():.2f}\n')

print('----------------------------------------------------\n')

#Section 4: Best Model
High_acc_index=dataset[1,::].argmax()

print('       --Best Model--\n')

print(f'Model Name: {models[High_acc_index]}')
print(f'Accuracy: {dataset[1,High_acc_index]}%')
print(f'Training Time: {dataset[2,High_acc_index]} mins')
print(f'Loss: {dataset[3,High_acc_index]}\n')

print('----------------------------------------------------\n')

#Section 5:Fastest Model
print('     --Fastest Model--\n')

Fastest_index=dataset[2,::].argmin()

print(f'Model Name: {models[Fastest_index]}')
print(f'Training Time: {dataset[2,Fastest_index]} mins')
print(f'Accuracy: {dataset[1,Fastest_index]}%\n')

print('----------------------------------------------------\n')

#Section 6:Lowest Loss Model
print('   --Lowest Loss Model--\n')
Lowloss_index=dataset[3,::].argmin()

print(f'Model Name: {models[Lowloss_index]}')
print(f'Loss: {dataset[3,Lowloss_index]}\n')

print('----------------------------------------------------\n')

#Section 7: Overall Rankings
print('       Overall Rankings\n')

Acc_wise=np.argsort(dataset[1,::])[::-1]

num=1
for i in Acc_wise:
    print(f'{num}.')
    print(f'Model: {models[i]}')
    print(f'Accuracy: {dataset[1,i]:.2f}%')
    print('--------------------------')
    num+=1

print('----------------------------------------------------\n')

#Section 8: Dataset Health Check

print('Dataset Health Check\n')

print(f'Highest Accuracy: {dataset[1,::].max()}')
print(f'Lowest Accuracy: {dataset[1,::].min()}')
print(f'Highest Loss: {dataset[3,::].max()}')
print(f'Lowest Loss: {dataset[3,::].min()}')
print(f'Highest Images: {dataset[0,::].max()}')
print(f'Lowest Images: {dataset[0,::].min()}\n')
print('----------------------------------------------------\n')


#Section 9: boolean Analysis

print('       Boolean Analysis\n')

print(f'Models with Accuracy >= 90%: {dataset[1,::][dataset[1,::]>=90].size}')
print(f'Models with Loss < 2: {dataset[3,::][dataset[3,::]<2].size}')
print(f'Models with Training Time < 130 mins: {dataset[2,::][dataset[2,::]<130].size}\n')

print('----------------------------------------------------\n')

# Section 10: Fine Tuning
dataset[1,::] = (dataset[1,::] * 1.02).round(2) #+2 Percent
dataset[0,::] = dataset[0,::] * 1.1 #+10 Percent
dataset[3,::] = dataset[3,::] * 0.85 #-15 percent

print('         After Fine Tuning \n')

print(f'New Average Accuracy: {dataset[1,::].mean():.2f}')
print(f'New Average Images Used: {dataset[0,::].mean():.2f}')
print(f'New Average Loss: {dataset[3,::].mean():.2f}\n')

print('----------------------------------------------------\n')

#Section 11:Saving as file

np.savetxt('Final_AI_Dataset.csv',dataset,delimiter=',',fmt='%.2f')

print('Updated Data Set is Saved as Final_AI_Dataset.csv !! \n')

print('====================================================')
print('          Report Generated Successfully')
print('====================================================\n')

import os
import random
import pandas as pd
from sklearn.model_selection import KFold



def Split_Sets_10_Fold(total_fold, data):
    train_index = []
    test_index = []
    train_scale, val_scale, test_scale = [0.8,0.2,0]
    kf = KFold(n_splits=total_fold, shuffle=True, random_state=0)
    i = 0

    for train_i, test_i in kf.split(data):
        i += 1
        num = str(i).zfill(2)
        train_index.append(train_i)
        test_index.append(test_i)
        print(train_index)
        train_data = data.iloc[train_i,:]
        data_test = data.iloc[test_i, :]

        # shuffle data
        df = train_data.sample(frac=1.0, random_state=0)
        rows, cols = df.shape
        data_train  = data_val = None


        val_idx = int(rows * val_scale)
        data_val: pd.DataFrame = df.iloc[0:val_idx, :]
        data_train: pd.DataFrame = df.iloc[val_idx: rows, :]

        file_name = 'NiH'+'_'+num
        extension = '.csv'


        test_folder = os.path.join(os.path.join('test'))
        make_dir(test_folder)
        test_file = test_folder + '//' + file_name + '_test' + extension
        data_test.to_csv(test_file, header=None, index=False)

        if val_scale > 0.0:
            val_folder = os.path.join(os.path.join('val'))
            make_dir(val_folder)
            val_file = val_folder + '//' + file_name + '_val' + extension
            data_val.to_csv(val_file, header=None, index=False)

        train_folder = os.path.join(os.path.join('train'))
        make_dir(train_folder)
        train_file = train_folder+'//'+file_name + '_train'+extension
        data_train.to_csv(train_file, header=None, index=False)

def make_dir(file_path):
    if os.path.isdir(file_path):
        pass
    else:
        os.makedirs(file_path)


if __name__ == "__main__":
    df = pd.read_excel('NiH.xlsx',skiprows=0)


    total_fold = 10
    Split_Sets_10_Fold(total_fold, df)
    # [train_index, test_index] = Split_Sets_10_Fold(total_fold, df)
    # train_data = df[train_index, :, :, :]
    # test_data = df[test_index, :,:,:]
    #
    # test_folder = os.path.join( 'test')


"""Functions for downloading and reading MNIST data."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os

import numpy
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin

import pandas as pd
import numpy as np

def extract_merged_axes(subject, window):
  filepath = '../../../../Prosjektoppgave/Notebook/data/'+subject+'/DATA_WINDOW/'+window+'/ORIGINAL/'
  files =   [
  'Axivity_BACK_Back_X.csv', 'Axivity_THIGH_Right_Y.csv', 
  'Axivity_BACK_Back_Y.csv', 'Axivity_THIGH_Right_Z.csv', 
  'Axivity_BACK_Back_Z.csv', 'Axivity_THIGH_Right_X.csv']
  df_0 = pd.read_csv(filepath+files[0], header=None, sep='\,',engine='python')
  df_1 = pd.read_csv(filepath+files[1], header=None, sep='\,',engine='python')
  df_2 = pd.read_csv(filepath+files[2], header=None, sep='\,',engine='python')
  df_3 = pd.read_csv(filepath+files[3], header=None, sep='\,',engine='python')
  df_4 = pd.read_csv(filepath+files[4], header=None, sep='\,',engine='python')
  df_5 = pd.read_csv(filepath+files[5], header=None, sep='\,',engine='python')

  df = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5],axis=1)
  return df.as_matrix(columns=None)

def extract_data(subjects, window):
  print('Extracting data from', subjects)

  train_data = extract_merged_axes(subjects[0], window)

  for i in range(1,len(subjects)):
    subject_data = extract_merged_axes(subjects[i], window)

    train_data = np.concatenate((train_data,subject_data ), axis=0)

  return train_data

def extract_merged_labels(subject, output_size, change_labels, window):
  filepath = '../../../../Prosjektoppgave/Notebook/data/'+subject+'/DATA_WINDOW/'+window+'/ORIGINAL/GoPro_LAB_All_L.csv'
  

  df = pd.read_csv(filepath, header=None, sep='\,',engine='python')

  # Convert from nunber to readable format: 
  # From: [2]
  # To: [0,1,0,0,0,0,0,0,0,0,0]
  m = []
  for i in range(len(df)):
    a = df.iloc[i]
    if change_labels:
      a = change_labels[a.values[0]]
    n =  np.zeros(output_size)
    n[a-1] = 1
    m.append(n)

  s = pd.DataFrame(m)


  return s.values


def extract_labels(subjects, output_size, change_labels, window):
  print('Extracting label from', subjects)
  train_label = extract_merged_labels(subjects[0], output_size, change_labels, window)

  for i in range(1,len(subjects)):
    subject_label = extract_merged_labels(subjects[i], output_size, change_labels, window)

    train_label = np.concatenate((train_label,subject_label ), axis=0)

  return train_label


def extract_merged_labels_and_data(subject, output_size, remove_activities, convert_activties, window, remove_messy_windows):
  filepath = '../../../../Prosjektoppgave/Notebook/data/'+subject+'/DATA_WINDOW/'+window+'/ORIGINAL/'
  files =   [
  'Axivity_CHEST_Back_X.csv', 'Axivity_THIGH_Right_Y.csv', 
  'Axivity_CHEST_Back_Y.csv', 'Axivity_THIGH_Right_Z.csv', 
  'Axivity_CHEST_Back_Z.csv', 'Axivity_THIGH_Right_X.csv']

  if remove_messy_windows:
    files =   [
    'Axivity_BACK_Back_X_REMOVED_MESSY_WINDOWS.csv', 'Axivity_THIGH_Right_Y_REMOVED_MESSY_WINDOWS.csv', 
    'Axivity_BACK_Back_Y_REMOVED_MESSY_WINDOWS.csv', 'Axivity_THIGH_Right_Z_REMOVED_MESSY_WINDOWS.csv', 
    'Axivity_BACK_Back_Z_REMOVED_MESSY_WINDOWS.csv', 'Axivity_THIGH_Right_X_REMOVED_MESSY_WINDOWS.csv']

  df_0 = pd.read_csv(filepath+files[0], header=None, sep='\,',engine='python')
  df_1 = pd.read_csv(filepath+files[1], header=None, sep='\,',engine='python')
  df_2 = pd.read_csv(filepath+files[2], header=None, sep='\,',engine='python')
  df_3 = pd.read_csv(filepath+files[3], header=None, sep='\,',engine='python')
  df_4 = pd.read_csv(filepath+files[4], header=None, sep='\,',engine='python')
  df_5 = pd.read_csv(filepath+files[5], header=None, sep='\,',engine='python')

  filepath = '../../../../Prosjektoppgave/Notebook/data/'+subject+'/DATA_WINDOW/'+window+'/ORIGINAL/GoPro_LAB_All_L.csv'
  if remove_messy_windows:
    filepath = '../../../../Prosjektoppgave/Notebook/data/'+subject+'/DATA_WINDOW/'+window+'/ORIGINAL/GoPro_LAB_All_L_REMOVED_MESSY_WINDOWS.csv'

  df_labels = pd.read_csv(filepath, header=None, sep='\,',engine='python')
  df_labels.columns = ['labels']
  df_data = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_labels],axis=1)

  for key, value in remove_activities.iteritems():
     df_data =  df_data[df_data['labels'] != key]
  df_labels = df_data['labels']
  df_data = df_data.drop('labels', 1)

  # Convert from nunber to readable format: 
  # From: [2]
  # To: [0,1,0,0,0,0,0,0,0,0,0]
  m = []
  for i in range(len(df_labels)):
    a = df_labels.iloc[i]
    n =  np.zeros(output_size)
    #print(a,n,convert_activties)
    n[convert_activties.get(a)-1] = 1
    m.append(n)

  df_labels = pd.DataFrame(m)

  return df_data.as_matrix(columns=None), df_labels.values

def extract_labels_and_data(subjects, output_size, remove_activities, convert_activties, window, remove_messy_windows):
  print('Extracting label and data set from', subjects)
  data, labels = extract_merged_labels_and_data(subjects[0], output_size, remove_activities, convert_activties, window, remove_messy_windows)

  # Iterate over all subjects
  for i in range(1,len(subjects)):
    sub_data, sub_labels = extract_merged_labels_and_data(subjects[i], output_size, remove_activities, convert_activties, window, remove_messy_windows)

    # Append data and labels
    data = np.concatenate((data,sub_data ), axis=0)
    labels = np.concatenate((labels, sub_labels), axis=0)

  return data, labels

def extract_data_without_activities_subject(subject, output_size, remove_activities, window):
  filepath = '../../../../Prosjektoppgave/Notebook/data/'+subject+'/DATA_WINDOW/'+window+'/ORIGINAL/'
  files =   [
  'Axivity_BACK_Back_X.csv', 'Axivity_THIGH_Right_Y.csv', 
  'Axivity_BACK_Back_Y.csv', 'Axivity_THIGH_Right_Z.csv', 
  'Axivity_BACK_Back_Z.csv', 'Axivity_THIGH_Right_X.csv']
  df_0 = pd.read_csv(filepath+files[0], header=None, sep='\,',engine='python')
  df_1 = pd.read_csv(filepath+files[1], header=None, sep='\,',engine='python')
  df_2 = pd.read_csv(filepath+files[2], header=None, sep='\,',engine='python')
  df_3 = pd.read_csv(filepath+files[3], header=None, sep='\,',engine='python')
  df_4 = pd.read_csv(filepath+files[4], header=None, sep='\,',engine='python')
  df_5 = pd.read_csv(filepath+files[5], header=None, sep='\,',engine='python')

  filepath = '../../../../Prosjektoppgave/Notebook/data/'+subject+'/DATA_WINDOW/'+window+'/ORIGINAL/GoPro_LAB_All_L.csv'

  df_labels = pd.read_csv(filepath, header=None, sep='\,',engine='python')
  df_labels.columns = ['labels']
  df_data = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_labels],axis=1)
  for key, value in remove_activities.iteritems():
     df_data =  df_data[df_data['labels'] != key]
  df_data = df_data.drop('labels', 1)
  return df_data.as_matrix(columns=None)

def extract_data_without_activities(subjects, output_size, remove_activities, window):
  print('Extracting data set from', subjects)
  data = extract_data_without_activities_subject(subjects[0], output_size, remove_activities, window)
  # Iterate over all subjects
  for i in range(1,len(subjects)):
    sub_data = extract_data_without_activities_subject(subjects[i], output_size, remove_activities, window)

    # Append data and labels
    data = np.concatenate((data,sub_data ), axis=0)

  return data

class DataSet(object):

  def __init__(self, data, labels=None):
    self._num_examples = data.shape[0]

    self._data = data
    self._labels = labels
    self._epochs_completed = 0
    self._index_in_epoch = 0

  def label_size(self):
      return len(self._labels)

  @property
  def data(self):
    return self._data

  @property
  def labels(self):
    return self._labels

  @property
  def num_examples(self):
    return self._num_examples

  @property
  def epochs_completed(self):
    return self._epochs_completed

  def shuffle_data_set(self):
    perm = numpy.arange(len(self._data))
    numpy.random.shuffle(perm)
    self._data = self._data[perm]
    self._labels = self._labels[perm]
    #print('Data set is shuffled')

  def next_batch(self, batch_size):
    """Return the next `batch_size` examples from this data set."""
   
    start = self._index_in_epoch
    self._index_in_epoch += batch_size
    if self._index_in_epoch > len(self._data):
      #print("Shuffle data set")
      # Finished epoch
      self._epochs_completed += 1
      # Shuffle the data
      perm = numpy.arange(len(self._data))
      numpy.random.shuffle(perm)
      self._data = self._data[perm]
      self._labels = self._labels[perm]
      # Start next epoch
      start = 0
      self._index_in_epoch = batch_size
      assert batch_size <= self._num_examples
    end = self._index_in_epoch
    return self._data[start:end], self._labels[start:end]

  def next_data_label(self, index):
    """Return the next `batch` examples from this data set."""
    if index > len(self._data):
      print('Test index is larger than data set', index)
      index = 0 

    return [self._data[index]], self._labels[index]


def move_data_from_test_to_train(prediction_indices, data_set):
  correct_relabeled = 0
  print(data_set.train._data.shape)
  new_data = np.zeros([len(prediction_indices), 600])
  new_label = np.zeros([len(prediction_indices),10])
  delete_indices = np.zeros(len(prediction_indices))

  ''' Sort data based on index '''
  #prediction_indices = sorted(prediction_indices, key=lambda row: row[0])
  for i in range(0,len(prediction_indices)):
    data = data_set.test._data[prediction_indices[i][0]]
    

    

    majority = True
    if majority:
      #predictions = []
      #for j in prediction_indices[i][1]:
      #  predictions.append(np.argmax(j))
      #acitivity = np.argmax(np.bincount(predictions))
      activity = prediction_indices[i][1]
    else: # max prediction
      activity = 0.0
      prediction = 0.0
      # From all the different classifiers, find the activity with the highest confident
      for j in range(0,len(prediction_indices[i][1])):
        temp_prediction = np.max(prediction_indices[i][1][j])
        if temp_prediction >= prediction:
          activity = np.argmax(prediction_indices[i][1][j])
          prediction = temp_prediction

    # Create label
    label = np.zeros(len(data_set.train._labels[0]))
    label[activity] = 1.0
    
    # Self learning
    label = data_set.test._labels[prediction_indices[i][0]]
    new_data[i] = data
    new_label[i] = label
    delete_indices[i] = prediction_indices[i][0]
    #print(temp_label, prediction_indices[i][0])
    # Count correct relabeling
    if np.argmax(label) == np.argmax(data_set.test._labels[prediction_indices[i][0]]):
      correct_relabeled += 1
    #else:
    #  print(np.argmax(label),np.argmax(data_set.test._labels[prediction_indices[i][0]]))
  print("Self learning!!!!!")
  print('Insert new samples')
  # Insert data and label into train data
  #data_set.train._data = np.insert(data_set.train._data, len(data_set.train._data), new_data, axis=0)
  data_set.train._data = new_data
  #data_set.train._labels = np.insert(data_set.train._labels, len(data_set.train._labels), new_label, axis=0)
  data_set.train._labels = new_label
  print('Delete new samples')
  # Delete data and label from test subject
  data_set.test._data = np.delete(data_set.test._data, delete_indices, axis=0)
  data_set.test._labels = np.delete(data_set.test._labels, delete_indices, axis=0)


  print('Shuffle new training data')
  data_set.train.shuffle_data_set()

  if correct_relabeled > 0:
    print('Correct relabel', correct_relabeled*1.0 / len(prediction_indices), "majority", majority)
  return data_set

def shuffle_data(above_threshold, data_set):

  print('Number of training data before shuffle',len(data_set.train._data))
  print('Number of training labels before shuffle',len(data_set.train._labels))
  print('Number of transition data before shuffle',len(data_set.transition._data))
  for i in range(len(above_threshold)-1,-1,-1):
    p = above_threshold[i]
    temp_label = np.zeros(len(data_set.train._labels[0]))
    temp_label[p[1]] = 1.0
    temp_data = data_set.transition._data[p[0]]

    data_set.transition._data = np.delete(data_set.transition._data, p[0], axis=0)
    data_set.train._data = np.insert(data_set.train._data, len(data_set.train._data), temp_data, axis=0)
    data_set.train._labels = np.insert(data_set.train._labels, len(data_set.train._labels), temp_label, axis = 0)

  print('Number of training data after shuffle',len(data_set.train._data))
  print('Number of training labels after shuffle',len(data_set.train._labels))
  print('Number of transition data after',len(data_set.transition._data))
  return data_set

def read_data_sets(subjects_set, output_size, change_labels, load_model, window):
  training_subjects = subjects_set[0]
  test_subjects = subjects_set[1]
  
  class DataSets(object):
    pass
  data_sets = DataSets()

  # If the model is for testing
  if load_model:
    # Testing data and labels
    test_data = extract_data(test_subjects, window)
    test_labels = extract_labels(test_subjects, output_size, change_labels, window)

    # Define testing data sets
    data_sets.test = DataSet(test_data, test_labels)

  else:
     # Training data and labels
    train_data = extract_data(training_subjects, window)
    train_labels = extract_labels(training_subjects, output_size, change_labels, window)

    # Testing data and labels
    test_data = extract_data(test_subjects,window)
    test_labels = extract_labels(test_subjects, output_size, change_labels, window)

    # Define training and testing data sets
    data_sets.train = DataSet(train_data, train_labels)
    data_sets.test = DataSet(test_data, test_labels)

  return data_sets


def read_data_sets_without_activity(subjects_set, output_size, remove_activities, load_model, convert_activties, window):
  training_subjects = subjects_set[0]
  test_subjects = subjects_set[1]
  remove_messy_windows = False
  oversampling = False
  validation_set = True

  print('Remove messy windows', remove_messy_windows)
  print('Oversampling', oversampling)
  print('Validation set', validation_set)

  class DataSets(object):
    pass
  data_sets = DataSets()

  # If the model is for testing
  if load_model:
    # Testing data and labels
    test_data, test_labels = extract_labels_and_data(test_subjects, output_size, remove_activities, convert_activties, window, remove_messy_windows)

    # Define testing data sets
    data_sets.test = DataSet(test_data, test_labels)

  else:
     # Training data and labels
    train_data, train_labels = extract_labels_and_data(training_subjects, output_size, remove_activities, convert_activties, window, remove_messy_windows)
    
    if oversampling:
      # length of longest activity
      max_length = 0
      activities = [0,1,2,3,4,5,6,7,8,9]
      for activity in activities:
        activity_length = sum(train_labels[::,activity])
        if activity_length > max_length:
          max_length = activity_length
      print(max_length)
      train_data_new = np.zeros([max_length * len(activities), 600])
      train_labels_new = np.zeros([max_length * len(activities), len(activities)])
      #print(train_labels[0:10], 'old')
      #print(train_labels_new[0:10], 'new')

      for i in range(0,len(activities)):
        activity_boolean = train_labels[::,i] == 1.0
        activity_data = train_data[activity_boolean]
        activity_label = train_labels[activity_boolean]

        activity_length = len(activity_data)
        print(activity_length)
        fraction = int(max_length / activity_length) + 1
        
        new_activity_data = np.tile(activity_data, (fraction, 1))
        new_activity_label = np.tile(activity_label, (fraction, 1))
        new_activity_data = new_activity_data[0:max_length]
        new_activity_label = new_activity_label[0:max_length]
        train_data_new[i*max_length:i*max_length+max_length] = new_activity_data
        train_labels_new[i*max_length:i*max_length+max_length] = new_activity_label

      for activity in activities:
        activity_length = sum(train_labels_new[::,activity])
        print(activity_length)
      # Testing data and labels
      train_data = train_data_new
      train_labels = train_labels_new
    test_data, test_labels = extract_labels_and_data(test_subjects, output_size, remove_activities, convert_activties, window, False)

    if validation_set:
      #Split test data into a test and validation part
      indices = np.arange(len(test_data))
      idx = np.random.choice(indices, len(test_data) / 2, replace=False)
      idx2 = np.setdiff1d(indices, idx)
      # Validation data
      validation_data = test_data[idx]
      validation_labels = test_labels[idx]
      # Test data
      test_data = test_data[idx2]
      test_labels = test_labels[idx2]
      
      data_sets.validation = DataSet(validation_data, validation_labels)

  # Define training and testing data sets
  data_sets.train = DataSet(train_data, train_labels)
  data_sets.test = DataSet(test_data, test_labels)


  return data_sets

def read_EM_data_set(subjects_set, output_size, train_remove_activities, train_convert, transition_remove_activties, window):
  class DataSets(object):
    pass
  data_sets = DataSets()

  training_subjects = subjects_set[0]
  transition_subjects = subjects_set[0]
  test_subjects = subjects_set[1]

  train_data, train_labels = extract_labels_and_data(training_subjects, output_size, train_remove_activities, train_convert, window)
  transition_data = extract_data_without_activities(transition_subjects, len(train_remove_activities), transition_remove_activties, window)

  test_data, test_labels = extract_labels_and_data(test_subjects, output_size, train_remove_activities, train_convert, window)

  data_sets.train = DataSet(train_data, train_labels)
  data_sets.train.shuffle_data_set()
  data_sets.transition = DataSet(transition_data)
  data_sets.test = DataSet(test_data, test_labels)

  return data_sets


''' Data set for Semi-supervised learning '''
def read_SS_data_set(subjects_set, output_size, convertion, window):
  class DataSets(object):
    pass
  data_sets = DataSets()
  training_subjects = subjects_set[0]
  test_subjects = subjects_set[1]

  train_data, train_labels = extract_labels_and_data(training_subjects, output_size, None, convertion, window)
  
  test_data, test_labels = extract_labels_and_data(test_subjects, output_size, None, convertion, window)
  
  #Split test data into a test and validation part
  indices = np.arange(len(test_data))
  idx = np.random.choice(indices, len(test_data) / 2, replace=False)
  idx2 = np.setdiff1d(indices, idx)
  # Validation data
  validation_data = test_data[idx]
  validation_labels = test_labels[idx]
  # Test data
  test_data = test_data[idx2]
  test_labels = test_labels[idx2]

  data_sets.train = DataSet(train_data, train_labels)
  data_sets.test = DataSet(test_data, test_labels)
  data_sets.validation = DataSet(validation_data, validation_labels)

  return data_sets
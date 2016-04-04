import data_generator
import CNN_STATIC_VARIABLES
import CNN_MOD_4
import numpy as np

class CNN_SS_TRAIN(object):
   """docstring for CNN_H"""
   def __init__(self, network_type, iterations, window, input_size, conv, nn, filter_type, number_of_classifiers):
      VARS = CNN_STATIC_VARIABLES.CNN_STATIC_VARS()
      subject_set = VARS.get_subject_set_SS(True)
      
     
      output = 10
      remove_activities = VARS.CONVERTION_STATIC_DYNAMIC_INVERSE
      keep_activities = VARS.CONVERTION_STATIC_DYNAMIC

      self.config = VARS.get_config(input_size, output, iterations, 100, network_type, conv, nn, filter_type)
      print 'Creating data set'
      self.data_set = data_generator.read_data_sets_without_activity(subject_set, output, remove_activities, None, keep_activities, window)
      self.data_set.train.shuffle_data_set()

      networks = []
      for i in range(0,number_of_classifiers):
         self.config['model_name'] = self.config['model_name'] + "_" + str(i)
         cnn = CNN_MOD_4.CNN_FILTER(self.config)
         cnn.set_data_set(self.data_set)
         cnn.train_network()
         cnn.test_network_stepwise()
         networks.append(cnn)

      ss_iterator = 0
      num_samples = 0
      while ss_iterator < 4:   
         prediction_steps = 10
         test_set_length = len(self.data_set.test._labels)
         threshold = 0.95
         # Returns an n-long array with random integer
         # integer range, length of array
         test_indecies = np.random.choice(test_set_length, test_set_length, replace=False)


         #print 'Predicting'
         prediction_indices = []
         for i in range(0, len(test_indecies)):
            # Get the data instance
            data = self.data_set.test._data[test_indecies[i]]
            # Predict the class label
            predictions = np.zeros((number_of_classifiers, output))    
            # Add the different prediction vectors to a list
            for j in range(0, number_of_classifiers):
               prediction = networks[j].run_network_return_probability([[data]])[0]
               predictions[j] = prediction
            
            # Check if the majority of the predictions are over the threshold
            if np.sum(predictions > threshold) >=  1:# np.ceil(number_of_classifiers*1.0 / 2):
               prediction_indices.append([test_indecies[i], predictions])

           
         print 'Number of new instances',len(prediction_indices)
         num_samples += len(prediction_indices)
         self.data_set = data_generator.move_data_from_test_to_train(prediction_indices, self.data_set)
        
         activity_accuracy = np.zeros(len(self.data_set.validation.labels[0]))
         for cnn in networks:
            cnn.set_data_set(self.data_set)
            cnn.train_network()
            cnn.test_network_stepwise()
         ss_iterator +=1       

      print 'Number of transfered instances', num_samples
      #self.cnn.save_model('models/' + network_type + '_' + str(input_size) + '_' + str(conv_f_1) + '_' + str(conv_f_2) + '_' + str(nn_1) + '_' + filter_type)


cnn_h = CNN_SS_TRAIN('original', 3000 , '1.0', 600, [20, 40], [200], "VALID", 1) 



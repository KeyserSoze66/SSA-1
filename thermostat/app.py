import paho.mqtt.client as mqtt #used to do MQTTS connection
import time #used to create a timer
import os #used to clear screen in Gui class
import random #used to create a random number

def create_ID():
      return("temp"+str(random.randrange(1001,9999)))

class Thermometer:
      def __init__(self, set_temperature, current_temperature, payload):
        '''set_temperature stores the value given by the controller the  
        heating is set to'''
        self.set_temperature = set_temperature
        self.current_temperature = current_temperature
        self.payload = payload
        
      def render_gui(self):
        '''this methods renders a GUI of a thermometer'''
        print("Set temperature:", self.set_temperature )
        print("Current temperature: ", self.current_temperature)
        print("----------------------------")
        
      def create_payload(self):
        '''the following if statement is to simulate that the measured 
        temperature is sometimes not as the set temperature.'''
        if random.randrange(0,5) == 3:
          self.current_temperature = self.set_temperature +1
        else:
          self.current_temperature = self.set_temperature
        self.payload = client_id + "actual--" + str(self.set_temperature)
            
      
client_id = create_ID() #create a random client ID
client = mqtt.Client() #create a MQTT client object
thermometer = Thermometer (20, 13, "lalala") #create a thermometer object


'''the following line of code is used to delay this programm / the node till 
the user connected this node to the Docker network. This is essential, since a 
MQTT connection to the broker can only be successfull, if the node is in the 
same network as the broker'''
any_var = input("integrate this node to the Docker network & then press Enter")

client.connect("nebula_mosquitto_container",1883,60) #connect to broker



while True: #loop forever
  '''communication sleeps to save battery power. A random value for sleeping 
  was chosen to simulate an unreliable node'''
  time.sleep(random.randrange(1,4)) 
  thermometer.create_payload() #create payload
  client.publish("home/temp", thermometer.payload) #publish payload
  thermometer.render_gui() #render the gui
  

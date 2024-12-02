import * as React from 'react';
import { Text, SafeAreaView, StyleSheet, Button, TouchableOpacity } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';
import Hello from './Page1';
import Helloagain from './Page2';
import SettingsScreen from './Settings';
const Stack = createStackNavigator();
const Tab= createBottomTabNavigator();
function HomeScreen({ navigation }) {
  return (
    <SafeAreaView>
      <Text>Home Screen</Text>
      <Button
        title="hey"
        onPress={() => { navigation.navigate("Home1"); }}
      />
      <TouchableOpacity onPress={()=>{navigation.navigate("Home2")}}>
      <Text style={{fontSize: 20}}>Sing to God with love</Text>
      </TouchableOpacity>
    </SafeAreaView>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} options={{ title: 'Welcome' }} />
        <Stack.Screen name="Home1" component={Hello} />
        <Stack.Screen name="Home2" component={Helloagain} />
        <Stack.Screen name="Tabs" components={myTabs} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

function myTabs() {
  return(
    <Tab.Navigator>
    <Tab.Screen name="feed" component={Hello}/>
    <Tab.Screen name="Settings" component={SettingsScreen} />
    </Tab.Navigator>
  );
}

const styles = StyleSheet.create({});

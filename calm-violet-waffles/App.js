import { Text, SafeAreaView, StyleSheet,Button, Switch, TextInput, Pressable, FlatList, ScrollView, TouchableOpacity,ActivityIndicator, TouchableHighlight, View, } from 'react-native';
import React from 'react';
import {useState} from 'react';
import {NavigationContainer} from '@react-navigation/native';

const handlepress=()=>{console.log("heloo freek bitches");}

export default function App() {
  const [number, setNumber]=useState(0);
  const [sibling, setSibling]=useState('Joe');
  const [onswitch, setOnswitch]=useState(false);
  const [text, onChangeText]=React.useState(null);
  const [number1, onChangeNumber]=React.useState(text);
  return (
    <NavigationContainer>
    <SafeAreaView style={styles.container}>
    <ScrollView>
   {/*<ActivityIndicator size="small" color="#000" />*/}
   <TouchableOpacity>
   <Text>Hello</Text>
   </TouchableOpacity>
   <TouchableHighlight>
   <Text>hi there</Text>
   </TouchableHighlight>
<Button title="press me"
onPress={()=>{alert("YOU CLICKED THE BUTTON, fuck you nigga");}}
color='orange'
/>
    <TextInput 
    value={text}
    placeholder="enter some text mtf"
    style={styles.style1}
    />
    <Switch 
    value={onswitch}
    onValueChange={(newValue)=>setOnswitch(newValue)}
    />
    <Pressable
    onPress={()=>{console.log("pressed");}}
    onPressIn={()=>{console.log("pressed in");}}
    onPressOut={()=>{console.log("pressed out");}}
    onLongPress={()=>{console.log("long press");}}
    >
    <Text>Pressable</Text>
    </Pressable>
    <TextInput 
    value={number1}
    onChangeText={onChangeNumber}
    style={styles.style1}
    keyboardType={'numeric'}
    placeholder="enter some numbers"
    />
      <Text style={styles.paragraph}>
        Change code in the editor and watch it change on your phone! Save to get a shareable url.
      </Text>
      <Button title='hellow world'
      onPress={()=>{console.log("hello to the effing world");}}
      />
      <Text>hi</Text>
      <Button title='bongo'
      onPress={handlepress}
      />
      <Text>hi {sibling}</Text>
      <Button title='grrr'
      onPress={()=>{setSibling(sibling === 'Joe' ? 'Romanus' : 'Joe');}}
      />
      <Text style={{fontSize:30}}>{number}</Text>
      <Button title='test usestate'
      onPress={()=>{setNumber(number+5)}}
      />
      </ScrollView>
    </SafeAreaView>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#ecf0f1',
    padding: 8,
  },
  paragraph: {
    margin: 24,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  style1:{
    height: 40,
    width: '80%',
    fontSize: 20,
    borderWidth: 2,
    alignSelf: 'center',
    color: 'green',
  }
});

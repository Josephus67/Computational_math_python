import { Text, SafeAreaView, StyleSheet,Button,View } from 'react-native';
import {useState} from 'react';
// You can import supported modules from npm
import { Card } from 'react-native-paper';

// or any files within the Snack
import AssetExample from './components/AssetExample';
const handlepress=()=>{console.log('hello world');}
export default function states() {
  const [number, setNumber]= useState(0);
  const [color, setColor]=useState('green');
  return (
    <SafeAreaView style={styles.container}>
    <Button title="reezy"
    onPress={()=>{setColor('blue')}}
    />
    <Text style={{fontSize:30}}>{color}</Text>
      <Text style={styles.paragraph}>
        Change code in the editor and watch it change on your phone! Save to get a shareable url.
      </Text>
      <View style={styles.number1}>
      <Text style={styles.number1}>{number}</Text>
      </View>
      <Button title="bingo"
      onPress={handlepress}
      />
      <Card>
        <AssetExample />
      </Card>
      <Button title="hello world"
      onPress={()=>{setNumber(number+1);}}
       />
    </SafeAreaView>
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
  number1:{
    fontSize: 40,
    fontWeight: 'bold',
  }
});

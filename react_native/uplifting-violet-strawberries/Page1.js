import React from 'react';
import {Text, View, StyleSheet,SafeAreaView} from 'react-native';

 const Hello=()=>{
   return(
<SafeAreaView style={styles.container}>
<Text>my soul is filled with joy</Text>
<Text>as i sing to God my saviour</Text>
<Text>he has looked upon his servants</Text>
<Text>He has visited his people</Text>
<Text>And holy is his name</Text>
</SafeAreaView>
   );
 }
 const styles=StyleSheet.create({
container: {
  backgroundColor: 'blue',
  height: '100%',
  
}
 }
 );
 export default Hello;
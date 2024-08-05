import React from 'react';
import {View, Text, StyleSheet,SafeAreaView} from 'react-native';

const Letsgo = () => {
    return(
        <SafeAreaView styles={styles.container}>
            <Text style={styles.text}>Let's Go!</Text>
            <Text style={styles.subText}>This is our first screen</Text>
            <Text>Whats up brothers</Text>
        </SafeAreaView>
    );
}
const styles= StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#f0f'
    },
    text: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#333',
    },
    subText: {
        fontSize: 18,
        color: '#666',
    }
});
export default Letsgo;
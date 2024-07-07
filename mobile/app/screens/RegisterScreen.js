import axios from 'axios';
import {View, Button, TextInput} from 'react-native';
import styles from '../styles/styles';
import Header from '../sections/header';
export const uri = "http://localhost:8000/";

export default function RegisterScreen() {
  state = {}
  console.log(state)
  function register(request) {
    const response = axios.post(`${uri}users/register`, request);
    return response
  }
  return (
    <View style={styles.top}>
      <Header/>
      <View style={styles.container}>
        <TextInput placeholder="Enter your Email Address" style={styles.input} onChangeText={(text) => state.email = text}/>
        <TextInput placeholder="Enter your Password" style={styles.input} secureTextEntry password onChangeText={(text) => state.password = text}/>
        <TextInput placeholder="Confirm your Password" style={styles.input} secureTextEntry password onChangeText={(text) => state.confirmpassword = text}/>
        <Button title="Register" color="blue" onPress={() => register(state)}/>
      </View>
    </View>
  );
}
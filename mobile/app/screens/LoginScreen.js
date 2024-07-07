import axios from 'axios';
import {View, Button, TextInput } from 'react-native';
import uri from '../config/env';
import Header from '../sections/header';
import styles from '../styles/styles';

export default function LoginScreen() {
  state = {}
  console.log(state)
  function login(request) {
    const response = axios.post(`${uri}users/login`, request).then((result) => {
      if (result.data.success)
        alert("Logged in")
      else
        alert(result.error)
    }).catch((err) => alert(err.message))
    return response
  }
  return (
    <View style={styles.top}>
      <Header/>
      <View style={styles.container}>
      <TextInput placeholder="Enter your Email Address" style={styles.input} onChangeText={(text) => state.email = text}/>
      <TextInput placeholder="Enter your Password" style={styles.input} secureTextEntry password onChangeText={(text) => state.password = text}/>
      <Button title="Log In" style={{color: 'orange'}} onPress={() => login(state)}/>
        Click here to Register
      </View>
    </View>
  );
}

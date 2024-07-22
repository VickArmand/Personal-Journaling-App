import axios from 'axios';
import {View, Button, TextInput } from 'react-native';
import uri from '../config/env';
import Header from '../sections/header';
import styles from '../styles/styles';

state = {}
async function login(request) {
  await axios.post(`${uri}users/login`, request).then((res) => {
    console.log(res)
    alert("Login success");
  }).catch((err) => alert(err.response.data.error));
}
export default function LoginScreen() {
  return (
    <View style={styles.top}>
      <Header/>
      <View style={styles.container}>
      <TextInput placeholder="Enter your Email Address" style={styles.input} onChangeText={(text) => state.email = text}/>
      <TextInput placeholder="Enter your Password" style={styles.input} secureTextEntry password onChangeText={(text) => state.password = text}/>
      <Button title="Log In" style={{color: 'orange'}} onPress={async () => await login(state)}/>
        Click here to Register
      </View>
    </View>
  );
}

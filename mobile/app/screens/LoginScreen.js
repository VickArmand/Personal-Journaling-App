import axios from 'axios';
import {View, Button, TextInput } from 'react-native';
import uri from '../config/env';
import Header from '../sections/header';
import styles from '../styles/styles';

state = {}
async function login(request) {
  await axios.post(`${uri}/users/login`, request).then((res) => {
    console.log(res)
    alert("Login success");
  }).catch((err) => alert(err.response.data.error));
}
async function logout(keys) {
  await axios.delete(`${uri}/users/logout`, {headers: {Cookie: `sessionid=${keys.session}; csrftoken=${keys.token};`, 'x-csrftoken': keys.token}}, {withCredentials: true}).then((res) => {
    console.log(res)
    alert(res.data.success);
  }).catch((err) => console.log(err));
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
      <Button title="Log Out" style={{color: 'orange'}} onPress={async () => await logout({session: "44334vla1q0u2rxain9btlvciybb11aa", token: "ixSxZBlC88LDtrp8p19IOhKZk6WhNiYhBtJg8HBZ17KcVFcxgdF0BIyFkMvI4P0d"})}/>
      </View>
    </View>
  );
}

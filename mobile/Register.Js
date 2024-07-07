import axios from 'axios';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
const uri = "http://localhost:8000/"
export default function App() {
  state = {}
  console.log(state)
  function register(request) {
    const response = axios.post(`${uri}users/register`, request);
    return response
  }
  return (
    <View style={styles.container}>
      <Text style= {styles.header}>PERSONAL JOURNALING APPLICATION</Text>
      <StatusBar style="auto" />
      <TextInput placeholder="Enter your Email Address" style={styles.input} onChangeText={(text) => state.email = text}/>
      <TextInput placeholder="Enter your Password" style={styles.input} secureTextEntry password onChangeText={(text) => state.password = text}/>
      <TextInput placeholder="Confirm your Password" style={styles.input} secureTextEntry password onChangeText={(text) => state.confirmpassword = text}/>
      <Button title="Register" color="blue" onPress={() => register(state)}/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginTop: 40,
    padding: 10,
    flex: 1,
    rowGap: 20,
    backgroundColor: '#fff',
  },
  header: {
    fontSize: 15,
    fontWeight: 'bold',
  },
  input: {
    padding: 10,
    borderWidth: 1,
    borderRadius: 3,
    height: 40,
    borderColor: 'orange',
  }
});

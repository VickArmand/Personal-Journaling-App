import axios from 'axios';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput, SafeAreaView } from 'react-native';
const uri = "http://localhost:8000/"
export default function App() {
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
      <StatusBar style="auto" />
      <SafeAreaView style={{backgroundColor:"orange", paddingTop: 40, paddingBottom: 20}}>
      <Text style= {styles.header}>PERSONAL JOURNALING APPLICATION</Text>
      </SafeAreaView>
      <View style={styles.container}>
      <TextInput placeholder="Enter your Email Address" style={styles.input} onChangeText={(text) => state.email = text}/>
      <TextInput placeholder="Enter your Password" style={styles.input} secureTextEntry password onChangeText={(text) => state.password = text}/>
      <Button title="Log In" style={{color: 'orange'}} onPress={() => login(state)}/>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  top: {
    flex: 1,
  },
  container: {
    marginTop: 20,
    padding: 10,
    flex: 1,
    rowGap: 20,
    backgroundColor: '#fff',
  },
  header: {
    fontSize: 15,
    fontWeight: 'bold',
    color: 'white',
    textAlign: 'center',
  },
  input: {
    padding: 10,
    borderWidth: 1,
    borderRadius: 3,
    height: 40,
    borderColor: 'blue',
  },
  button: {
    padding: 10,
  }
});

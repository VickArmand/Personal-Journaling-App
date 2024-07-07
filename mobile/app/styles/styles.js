import { StyleSheet, StatusBar, Platform } from 'react-native';

export default styles = StyleSheet.create({
    top: {
      flex: 1,
    },
    safearea: {
      backgroundColor:"orange",
      paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0,
      paddingBottom: Platform.OS === "android" ? 20 : 0
    },
    container: {
      marginTop: 20,
      padding: 10,
      display: 'flex',
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

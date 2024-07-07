import {Text, View, SafeAreaView, StatusBar } from 'react-native';

export default function Header() {
    return (
        <View>
            <StatusBar style="auto" />
            <SafeAreaView style={styles.safearea}>
            <Text style= {styles.header}>PERSONAL JOURNALING APPLICATION</Text>
            </SafeAreaView>
        </View>
    );
}
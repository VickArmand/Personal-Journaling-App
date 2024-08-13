import React from 'react';

const config = {
    headers: { Authorization: `Bearer ${tokens.accesstoken}` }
};
async function logout() {
    await axios.delete(`${uri}/users/logout`, config).then((res) => {
      console.log(res)
      alert(res.data.success);
    }).catch((err) => console.log(err));
}
function DashboardScreen(props) {
    return (
        <div>
            
        </div>
    );
}
const styles = StyleSheet.create({
    
})
export default DashboardScreen;
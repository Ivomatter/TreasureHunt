import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native'; // Import Text component from react-native

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("http://localhost:5000/members")
      .then(res => res.json())
      .then(data => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <View>
      {typeof data.members === 'undefined' ? (
        <View>
          <Text>Loading...</Text>
        </View>
      ) : (
        data.members.map((member, i) => (
          <Text key={i}>{member} AAAAAAAAAAAAAAAaTEST</Text> // Render each member inside Text component
        ))
      )}
    </View>
  );
}

export default App; 
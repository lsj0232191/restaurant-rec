import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';

const HomeScreen = () => {
  const [groupName, setGroupName] = useState('');
  const [groups, setGroups] = useState([]);

  const createGroup = () => {
    if (groupName.trim() !== '') {
      setGroups([...groups, groupName]);
      setGroupName('');
    }
  };

  return (
    <View>
      <Text>Create Groups</Text>
      <TextInput
        placeholder="Enter group name"
        value={groupName}
        onChangeText={(text) => setGroupName(text)}
      />
      <Button title="Create Group" onPress={createGroup} />
      <Text>Groups:</Text>
      {groups.map((group, index) => (
        <Text key={index}>{group}</Text>
      ))}
    </View>
  );
};

export default HomeScreen;

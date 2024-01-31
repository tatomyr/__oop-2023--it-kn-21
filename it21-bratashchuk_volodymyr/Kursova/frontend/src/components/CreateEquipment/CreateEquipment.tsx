import { useState } from 'react';
import { mainContentStore } from '../../stores/MainContentStore';
import { observer } from 'mobx-react-lite';
import { Loader } from '../Loader/Loader';

export const CreateEquipmentForm = observer(() => {
  const [name, setName] = useState('');
  const [type, setType] = useState('tractor');

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    mainContentStore.createEquipment(name, type);
  };

  if (mainContentStore.isCreating) {
    return <Loader />;
  }
  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" required />
      <select value={type} onChange={(e) => setType(e.target.value)}>
        <option value="tractor">Tractor</option>
        <option value="harvester">Harvester</option>
      </select>
      <button type="submit">Create</button>
    </form>
  );
});

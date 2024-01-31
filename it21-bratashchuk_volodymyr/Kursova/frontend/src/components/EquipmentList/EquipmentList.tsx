import { mainContentStore } from '../../stores/MainContentStore';
import { observer } from 'mobx-react-lite';

export const EquipmentList = observer(() => {
  return (
    <div>
      {mainContentStore.stats.map((equipment) => (
        <div key={equipment.equipment_id}>
          {equipment.name} | Type: {equipment.type}{' '}
          <button onClick={() => mainContentStore.deleteEquipment(equipment.equipment_id)}>Delete</button>
        </div>
      ))}
    </div>
  );
});

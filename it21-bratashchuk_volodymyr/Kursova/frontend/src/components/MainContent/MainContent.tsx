import { useEffect } from 'react';
import { Bar } from 'react-chartjs-2';
import { mainContentStore } from '../../stores/MainContentStore';
import { observer } from 'mobx-react-lite';
import { Loader } from '../Loader/Loader';
import { EquipmentList } from '../EquipmentList/EquipmentList';
import { CreateEquipmentForm } from '../CreateEquipment/CreateEquipment';

const options = {
  plugins: {
    title: {
      display: true,
      text: 'Chart.js Bar Chart - Stacked',
    },
  },
  responsive: true,
  scales: {
    x: {
      stacked: true,
    },
    y: {
      stacked: true,
    },
  },
};
const MainContent = observer(() => {
  useEffect(() => {
    mainContentStore.loadStats();
  }, []);

  const labels = mainContentStore.stats.map((el) => el.name);

  const data = {
    labels,
    datasets: [
      {
        label: 'Tractor',
        //   data: labels.map(() => faker.datatype.number({ min: 0, max: 1000 })),
        data: mainContentStore.stats.filter((el) => el.type === 'Tractor').map((el) => el.rental_count),

        backgroundColor: 'rgb(255, 99, 132)',
      },
      {
        label: 'Harvester',
        //   data: labels.map(() => faker.datatype.number({ min: 0, max: 1000 })),
        data: mainContentStore.stats.filter((el) => el.type === 'Harvester').map((el) => el.rental_count),

        backgroundColor: 'rgb(255, 0, 255)',
      },
    ],
  };

  if (mainContentStore.isLoading) {
    return (
      <div>
        <h1>Статистика Використання Обладнання</h1>
        <Loader />
      </div>
    );
  }

  return (
    <div>
      <h1>Статистика Використання Обладнання</h1>
      <Bar data={data} options={options} />
      <div className="controll-container">
        <EquipmentList /> <CreateEquipmentForm />
      </div>
    </div>
  );
});

export default MainContent;

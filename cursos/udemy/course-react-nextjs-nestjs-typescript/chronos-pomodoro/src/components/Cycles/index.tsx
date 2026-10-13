import { useTaskContext } from '../../contexts/TaskContext/useTaskContext';
import styles from './styles.module.css';

export function Cycles() {
  const { state } = useTaskContext();

  const cycledescriptionMap = {
    workTime: 'Foco',
    shortBreakTime: 'Descanso Curto',
    longBreakTime: 'Descanso Longo',
  };

  return (
    <div className={styles.cycles}>
      <span>Ciclos:</span>

      <div className={styles.cycleDots}>
        {state.tasks.map((task, index) => (
          <span
            key={index}
            title={`Indicador de ciclo de ${cycledescriptionMap[task.type]}`}
            aria-label='Indicador de ciclo'
            className={`${styles.cycleDot} ${styles[task.type]}`}
          ></span>
        ))}
      </div>
    </div>
  );
}

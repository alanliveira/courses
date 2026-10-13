import { useTaskContext } from '../../contexts/TaskContext/useTaskContext';
import { getNextCycle } from '../../utils/getnextCycle';
import { getNextCycleType } from '../../utils/getNextCycleType';

export function Tips() {
  const { state } = useTaskContext();

  const nextCycle = getNextCycle(state.currentCycle);
  const nextCycleType = getNextCycleType(nextCycle);

  return (
    <>
      {!!state.activeTask && (
        <p>
          Próximo ciclo é de{' '}
          <strong>{state.config[state.activeTask.type]} min</strong>
        </p>
      )}
      {!state.activeTask && (
        <p>
          Próximo intervalo é de{' '}
          <strong>{state.config[nextCycleType]} min</strong>
        </p>
      )}
    </>
  );
}

import { useEffect, useState } from 'react';
import { TrashIcon } from 'lucide-react';

import { Container } from '../../components/Container';
import { DefaultButton } from '../../components/DefaultButton';
import { Heading } from '../../components/Heading';
import { MainTemplate } from '../../templates/MainTemplate';
import { useTaskContext } from '../../contexts/TaskContext/useTaskContext';
import { formatDate } from '../../utils/formatDate';
import { getTaskStatus } from '../../utils/getTaskStatus';
import { sortTasks, SortTasksOptions } from '../../utils/sortTask';
import { TaskActionsTypes } from '../../contexts/TaskContext/taskActions';
import { showMessage } from '../../components/adapters/showMessage';

import style from './style.module.css';

export function History() {
  const { state, dispatchState } = useTaskContext();
  const [confirmClearHistory, setConfirmClearHistory] = useState(false);
  const hasTasks = state.tasks.length ? true : false;

  const [sortTaskOptions, setSortTaskOptions] = useState<SortTasksOptions>(
    () => {
      return {
        tasks: sortTasks({ tasks: state.tasks }),
        field: 'startDate',
        direction: 'desc',
      };
    },
  );

  useEffect(() => {
    setSortTaskOptions(prevState => ({
      ...prevState,
      tasks: sortTasks({
        tasks: state.tasks,
        direction: prevState.direction,
        field: prevState.field,
      }),
    }));
  }, [state.tasks]);

  useEffect(() => {
    if (!confirmClearHistory) return;

    setConfirmClearHistory(false);
  }, [confirmClearHistory, dispatchState]);

  useEffect(() => {
    document.title = 'Histórico - Chronos Pomodoro';

    return () => {
      showMessage.dismiss();
    };
  }, []);

  function handleShortTask({ field }: Pick<SortTasksOptions, 'field'>) {
    const newDirection: SortTasksOptions['direction'] =
      sortTaskOptions.direction === 'desc' ? 'asc' : 'desc';
    setSortTaskOptions({
      tasks: sortTasks({
        direction: newDirection,
        tasks: sortTaskOptions.tasks,
        field,
      }),
      direction: newDirection,
      field,
    });
  }

  function handleResetHistory() {
    // if (!confirm('Tem certeza')) return;
    showMessage.dismiss();
    showMessage.confirm('Te, certeza?', confirmation => {
      setConfirmClearHistory(confirmation);

      if (confirmation) dispatchState({ type: TaskActionsTypes.RESET_STATE });
    });
  }

  return (
    <MainTemplate>
      <Container>
        <Heading>
          <span>History</span>
          <span className={style.buttonContainer}>
            <DefaultButton
              color='red'
              icon={<TrashIcon />}
              aria-label='Apagar todo o histórico'
              title='Apagar Histórico'
              onClick={() => handleResetHistory()}
            />
          </span>
        </Heading>
      </Container>

      <Container>
        {hasTasks && (
          <div className={style.responsiveTable}>
            <table>
              <thead>
                <tr>
                  <th
                    className={style.thSort}
                    onClick={() => handleShortTask({ field: 'id' })}
                  >
                    Tarefa
                  </th>
                  <th
                    className={style.thSort}
                    onClick={() => handleShortTask({ field: 'duration' })}
                  >
                    Duração
                  </th>
                  <th
                    className={style.thSort}
                    onClick={() => handleShortTask({ field: 'startDate' })}
                  >
                    Data
                  </th>
                  <th>Status</th>
                  <th>Tipo</th>
                </tr>
              </thead>
              <tbody>
                {sortTaskOptions.tasks.map(task => {
                  const taskTypeDictionary = {
                    workTime: 'Foco',
                    shortBreakTime: 'Descanso Curto',
                    longBreakTime: 'Descanso Longo',
                  };

                  return (
                    <tr key={task.id}>
                      <td>{task.name}</td>
                      <td>{task.duration}</td>
                      <td>{formatDate(task.startDate)}</td>
                      <td>{getTaskStatus(task, state.activeTask)}</td>
                      <td>{taskTypeDictionary[task.type]}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
        {!hasTasks && (
          <p style={{ textAlign: 'center', fontWeight: 'bolder' }}>
            Ainda não existem tarefas criadas
          </p>
        )}
      </Container>
    </MainTemplate>
  );
}

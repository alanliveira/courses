import React, { useRef } from 'react';
import { PauseCircleIcon, PlayCircleIcon } from 'lucide-react';

import { Cycles } from '../Cycles';
import { DefaultButton } from '../DefaultButton';
import { DefaultInput } from '../DefaultInput';
import { TaskModel } from '../../models/TaskModel';
import { useTaskContext } from '../../contexts/TaskContext/useTaskContext';
import { getNextCycle } from '../../utils/getnextCycle';
import { getNextCycleType } from '../../utils/getNextCycleType';
import { TaskActionsTypes } from '../../contexts/TaskContext/taskActions';
import { Tips } from '../tips';
import { showMessage } from '../adapters/showMessage';

import style from './style.module.css';

export function MainForm() {
  const { state, dispatchState } = useTaskContext();
  const taskNameInput = useRef<HTMLInputElement>(null);
  const lastTaskName = state.tasks[state.tasks.length - 1]?.name || '';

  const nextCycle = getNextCycle(state.currentCycle);
  const nextCycleType = getNextCycleType(nextCycle);

  function handleCreateNewTask(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (taskNameInput.current === null) return;

    const taskName = taskNameInput.current.value.trim();

    if (!taskName) {
      showMessage.info('Digite o nome da tarefa');
      return;
    }

    showMessage.dismiss();

    const newTask: TaskModel = {
      id: Date.now().toString(),
      name: taskName,
      startDate: Date.now(),
      completeDate: null,
      interruptDate: null,
      duration: state.config[nextCycleType],
      type: nextCycleType,
    };

    dispatchState({ type: TaskActionsTypes.START_TASK, payload: newTask });
    showMessage.success('Tarefa iniciada');
  }

  function handleInterruptTask(
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>,
  ) {
    e.preventDefault();
    showMessage.dismiss();

    dispatchState({ type: TaskActionsTypes.INTERRUPT_TASK });

    showMessage.error('Tarefa interrompida');
  }

  return (
    <form onSubmit={handleCreateNewTask} className={style.form} action=''>
      <div className={style.formRow}>
        <DefaultInput
          labelText='task'
          id='meuInput'
          type='text'
          placeholder='Digite algo'
          ref={taskNameInput}
          disabled={!!state.activeTask}
          defaultValue={lastTaskName}
        />
      </div>

      <div className={style.formRow}>
        <Tips />
      </div>

      {state.tasks.length > 0 && (
        <div className={style.formRow}>
          <Cycles />
        </div>
      )}

      <div className={style.formRow}>
        {!state.activeTask && (
          <DefaultButton
            aria-label='Iniciar nova tarefa'
            title='Iniciar nova tarefa'
            type='submit'
            icon={<PlayCircleIcon />}
            key='botao_submit'
          />
        )}
        {!!state.activeTask && (
          <DefaultButton
            aria-label='Iniciar nova tarefa'
            title='Iniciar nova tarefa'
            type='button'
            color='red'
            onClick={e => handleInterruptTask(e)}
            icon={<PauseCircleIcon />}
            key='botao_button'
          />
        )}
      </div>
    </form>
  );
}

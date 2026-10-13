import { TaskStateModel } from '../../models/TaskStateModel';
import { formatSecondsToMinutes } from '../../utils/formatSecondsToMinutes';
import { getNextCycle } from '../../utils/getnextCycle';
import { initialTaskState } from './initialTaskState';
import { TaskActionModel, TaskActionsTypes } from './taskActions';

export function taskReducer(
  state: TaskStateModel,
  action: TaskActionModel,
): TaskStateModel {
  switch (action.type) {
    case TaskActionsTypes.START_TASK: {
      const activeTask = action.payload;
      const secondsRemaining = activeTask.duration * 60;
      const currentCycle = getNextCycle(state.currentCycle);
      const formattedSecondsRemaining =
        formatSecondsToMinutes(secondsRemaining);
      const tasks = [...state.tasks, activeTask];

      return {
        ...state,
        activeTask,
        currentCycle,
        secondsRemaining,
        formattedSecondsRemaining,
        tasks,
      };
    }
    case TaskActionsTypes.INTERRUPT_TASK: {
      const tasks = state.tasks.map(task => {
        if (task.id === state?.activeTask?.id) {
          task.interruptDate = Date.now();
        }

        return task;
      });

      return {
        ...state,
        activeTask: null,
        secondsRemaining: 0,
        formattedSecondsRemaining: '00:00',
        tasks,
      };
    }
    case TaskActionsTypes.COUNT_DOWN: {
      return {
        ...state,
        secondsRemaining: action.payload.secondsRemaining,
        formattedSecondsRemaining: formatSecondsToMinutes(
          action.payload.secondsRemaining,
        ),
      };
    }
    case TaskActionsTypes.COMPLETED_TASK: {
      const tasks = state.tasks.map(task => {
        if (task.id === state?.activeTask?.id) {
          task.completeDate = Date.now();
        }

        return task;
      });

      return {
        ...state,
        activeTask: null,
        secondsRemaining: 0,
        formattedSecondsRemaining: '00:00',
        tasks,
      };
    }
    case TaskActionsTypes.RESET_STATE:
      return { ...initialTaskState };
    case TaskActionsTypes.CHANGE_SETTINGS: {
      return { ...state, config: { ...action.payload } };
    }
    default:
      return state;
  }
}

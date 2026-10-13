import { createContext } from 'react';
import { TaskStateModel } from '../../models/TaskStateModel';
import { initialTaskState } from './initialTaskState';
import { TaskActionModel } from './taskActions';

type TaskContextProps = {
  state: TaskStateModel;
  dispatchState: React.Dispatch<TaskActionModel>;
};

const initialContextValue = {
  state: initialTaskState,
  dispatchState: () => {},
};

export const TaskContext = createContext<TaskContextProps>(initialContextValue);

import { useEffect, useRef } from 'react';
import { SaveIcon } from 'lucide-react';

import { useTaskContext } from '../../contexts/TaskContext/useTaskContext';
import { Container } from '../../components/Container';
import { DefaultButton } from '../../components/DefaultButton';
import { DefaultInput } from '../../components/DefaultInput';
import { Heading } from '../../components/Heading';
import { MainTemplate } from '../../templates/MainTemplate';
import { showMessage } from '../../components/adapters/showMessage';

import style from './style.module.css';
import { TaskActionsTypes } from '../../contexts/TaskContext/taskActions';

export function Settings() {
  const { state, dispatchState } = useTaskContext();

  const workTimeInputRef = useRef<HTMLInputElement | null>(null);
  const shortBreakTimeInputRef = useRef<HTMLInputElement | null>(null);
  const longBreakTimeInputRef = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    document.title = 'Configurações - Chronos Pomodoro';
  }, []);

  function handleSaveSettings(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const formErrors = [];

    const workTime = Number(workTimeInputRef.current?.value);
    const shortBreakTime = Number(shortBreakTimeInputRef.current?.value);
    const longBreakTime = Number(longBreakTimeInputRef.current?.value);

    showMessage.dismiss();

    if (isNaN(workTime))
      formErrors.push('Por favor use apenas números para foco!');

    if (isNaN(shortBreakTime))
      formErrors.push('Por favor use apenas números para descanso curto!');

    if (isNaN(longBreakTime))
      formErrors.push('Por favor use apenas números para descanso longo!');

    if (workTime < 1 || workTime > 99)
      formErrors.push('Digite valores entre 1 e 99 para foco!');

    if (shortBreakTime < 1 || shortBreakTime > 30)
      formErrors.push('Digite valores entre 1 e 99 para foco!');

    if (longBreakTime < 1 || longBreakTime > 60)
      formErrors.push('Digite valores entre 1 e 99 para foco!');

    if (formErrors.length > 0) {
      formErrors.forEach(error => {
        showMessage.error(error);
      });
      return;
    }

    dispatchState({
      type: TaskActionsTypes.CHANGE_SETTINGS,
      payload: { workTime, shortBreakTime, longBreakTime },
    });
    showMessage.success('Configurações salvas!');
  }

  return (
    <MainTemplate>
      <Container>
        <Heading>Configurações</Heading>
      </Container>

      <Container>
        <p style={{ textAlign: 'center' }}>
          Modifique as configurações para tempo de foco, descanso curto e
          descanso longo.
        </p>
      </Container>
      <Container>
        <form
          onSubmit={e => handleSaveSettings(e)}
          action=''
          className={style.form}
        >
          <div className={style.formRow}>
            <DefaultInput
              id='workTime'
              labelText='Foco'
              ref={workTimeInputRef}
              defaultValue={state.config.workTime}
              type='number'
              min={0}
              max={99}
              maxLength={2}
              step={5}
            />
          </div>
          <div className={style.formRow}>
            <DefaultInput
              id='shortBreakTime'
              labelText='Descanso Curto'
              ref={shortBreakTimeInputRef}
              defaultValue={state.config.shortBreakTime}
              type='number'
              min={0}
              max={30}
              maxLength={2}
              step={5}
            />
          </div>
          <div className={style.formRow}>
            <DefaultInput
              id='longBreakTime'
              labelText='Descanso Longo'
              ref={longBreakTimeInputRef}
              defaultValue={state.config.longBreakTime}
              type='number'
              min={0}
              max={60}
              maxLength={2}
              step={5}
            />
          </div>
          <div className={style.formRow}>
            <DefaultButton
              icon={<SaveIcon />}
              aria-label='Salvar Configurações'
              title='Salvar Configurações'
            />
          </div>
        </form>
      </Container>
    </MainTemplate>
  );
}

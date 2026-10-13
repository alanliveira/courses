import { ReactNode } from 'react';
import { Bounce, ToastContainer } from 'react-toastify';

type messageContainerProps = {
  children: ReactNode;
};

export function MessageContainer({ children }: messageContainerProps) {
  return (
    <>
      <ToastContainer
        position='top-center'
        autoClose={10_000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick={true}
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme='light'
        transition={Bounce}
      />

      {children}
    </>
  );
}

import MenuAdminComponent from '@/components/admin/MenuAdmin';
import { ReactNode } from 'react';

type AdminPostProps = {
  children: ReactNode;
};

export default function AdminPostLayout({
  children,
}: Readonly<AdminPostProps>) {
  return (
    <>
      <MenuAdminComponent />
      {children}
    </>
  );
}

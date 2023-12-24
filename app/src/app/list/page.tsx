import type { Metadata } from 'next';

import { Section } from '@/components';

export const metadata: Metadata = {
  title: 'Listar produtos',
  description: 'Listar produtos'
};

export default function listProductsPage() {
  return (
    <>
      <Section title="Listar produtos"></Section>
    </>
  );
}

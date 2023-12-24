import type { Metadata } from 'next';

import { Section } from '@/components';

export const metadata: Metadata = {
  title: 'Atualizar produto',
  description: 'Atualizar produto'
};

export default function updateProductsPage() {
  return (
    <>
      <Section title="Atualizar produto"></Section>
    </>
  );
}

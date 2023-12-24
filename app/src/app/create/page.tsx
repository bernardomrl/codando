import type { Metadata } from 'next';

import { Section } from '@/components';

export const metadata: Metadata = {
  title: 'Criar produto',
  description: 'Criar produto'
};

export default function createProductsPage() {
  return (
    <>
      <Section title="Criar produtos"></Section>
    </>
  );
}

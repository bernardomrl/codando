import type { Metadata } from 'next';

import { Section } from '@/components';

export const metadata: Metadata = {
  title: 'Apagar produto',
  description: 'Apagar produto'
};

export default function deleteProductsPage() {
  return (
    <>
      <Section title="Apagar produtos"></Section>
    </>
  );
}

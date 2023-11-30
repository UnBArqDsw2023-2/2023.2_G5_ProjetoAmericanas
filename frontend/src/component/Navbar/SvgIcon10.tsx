import { memo, SVGProps } from 'react';

const SvgIcon10 = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 11 18' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <g clipPath='url(#clip0_781_414)'>
      <path
        d='M2.74364 0.5L1.78909 1.45455L5.88 5.5L9.97091 1.45455L9.01637 0.5L5.88 3.59091L2.74364 0.5Z'
        fill='#333333'
      />
    </g>
    <defs>
      <clipPath id='clip0_781_414'>
        <rect width={10} height={17} fill='white' transform='translate(0.880005 0.5)' />
      </clipPath>
    </defs>
  </svg>
);

const Memo = memo(SvgIcon10);
export { Memo as SvgIcon10 };

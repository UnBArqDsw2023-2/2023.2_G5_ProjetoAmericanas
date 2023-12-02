import { memo, SVGProps } from 'react';

const SvgIcon4 = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 11 8' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <g clipPath='url(#clip0_781_400)'>
      <path
        d='M2.07758 0.5L0.910912 1.83636L5.91091 7.5L10.9109 1.83636L9.74425 0.5L5.91091 4.82727L2.07758 0.5Z'
        fill='white'
      />
    </g>
    <defs>
      <clipPath id='clip0_781_400'>
        <rect width={10} height={7} fill='white' transform='translate(0.82 0.5)' />
      </clipPath>
    </defs>
  </svg>
);

const Memo = memo(SvgIcon4);
export { Memo as SvgIcon4 };

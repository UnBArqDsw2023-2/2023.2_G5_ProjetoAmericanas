import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import { LinkSvgIcon } from './LinkSvgIcon.js';
import classes from './Navbar.module.css';
import { SvgIcon2 } from './SvgIcon2.js';
import { SvgIcon3 } from './SvgIcon3.js';
import { SvgIcon4 } from './SvgIcon4.js';
import { SvgIcon5 } from './SvgIcon5.js';
import { SvgIcon6 } from './SvgIcon6.js';
import { SvgIcon7 } from './SvgIcon7.js';
import { SvgIcon8 } from './SvgIcon8.js';
import { SvgIcon9 } from './SvgIcon9.js';
import { SvgIcon10 } from './SvgIcon10.js';
import { SvgIcon } from './SvgIcon.js';
import { Link } from 'react-router-dom';

interface Props {
  className?: string;
}
export const Navbar: FC<Props> = memo(function Navbar(props = {}) {
  return (
    <div className={`${resets.clapyResets} ${classes.root}`}>
      <div className={classes.divSrc__ContainerScQ7wx4i3}>
        <div className={classes.divTop__ContainerSc1usje8}>
          <Link to="/">
            <div className={classes.link}>
              <div className={classes.sVG}>
                <SvgIcon className={classes.icon} />
              </div>
            </div>
          </Link>
          <div className={classes.divSearch__ContainerSc1wvs0c1}>
            <div className={classes.form}>
              <div className={classes.inputPesquisar}>
                <div className={classes.divPlaceholder}>
                  <div className={classes.busqueAquiSeuProduto}>busque aqui seu produto</div>
                </div>
              </div>
              <div className={classes.buttonPesquisar}>
                <div className={classes.sVG2}>
                  <SvgIcon2 className={classes.icon2} />
                </div>
              </div>
            </div>
          </div>
          <div className={classes.divLogin__ContainerScRx2iwu}>
            <div className={classes.button}>
              <div className={classes.sVG3}>
                <SvgIcon3 className={classes.icon3} />
              </div>
              <div className={classes.spanLogin__TextScGbi31q}>
                <div className={classes.olaPhilipe}>olá, Usuario.</div>
                <div className={classes.spanLogin__SpanScGbi31q2}>
                  <div className={classes.minhaConta}>minha conta </div>
                  <div className={classes.sVG4}>
                    <SvgIcon4 className={classes.icon4} />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className={classes.divIconMenu__IconMenuContainer}>
            <div className={classes.link2}>
              <div className={classes.sVG5}>
                <SvgIcon5 className={classes.icon5} />
              </div>
            </div>
            <div className={classes.linkMargin}>
              <div className={classes.linkSVG}>
                <LinkSvgIcon className={classes.icon6} />
              </div>
            </div>
            <div className={classes.buttonMargin}>
              <div className={classes.button2}>
                <div className={classes.sVG6}>
                  <SvgIcon6 className={classes.icon7} />
                </div>
                <div className={classes.divIconMenu__BagdeBasketItemsS}>
                  <div className={classes.unnamed}>0</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className={classes.main}>
          <div className={classes.divCep__CepWrapperSc1cuzzxo4}>
            <div className={classes.button3}>
              <div className={classes.sVG7}>
                <SvgIcon7 className={classes.icon8} />
              </div>
              <div className={classes.pCep__TextSc1cuzzxo3}>
                <div className={classes.strongInformeSeuCEP}>informe seu CEP</div>
              </div>
            </div>
          </div>
          <div className={classes.list}>
            <div className={classes.itemLink}>
              <div className={classes.praSuaEmpresa}>pra sua empresa</div>
            </div>
            <div className={classes.itemLink2}>
              <div className={classes.baixeOApp}>baixe o app</div>
            </div>
            <div className={classes.itemLink3}>
              <div className={classes.entregaRapida}>entrega rápida</div>
            </div>
            <div className={classes.itemLink4}>
              <div className={classes.nossasLojas}>nossas lojas</div>
            </div>
            <div className={classes.itemLink5}>
              <div className={classes.dinheiroDeVolta}>dinheiro de volta</div>
            </div>
            <div className={classes.itemLink6}>
              <div className={classes.lojasOficiais}>lojas oficiais</div>
            </div>
            <div className={classes.itemLink7}>
              <div className={classes.marcasProprias}>marcas próprias</div>
            </div>
            <div className={classes.itemLink8}>
              <div className={classes.servicos}>serviços</div>
            </div>
            <div className={classes.itemLink9}>
              <div className={classes.sVG8}>
                <SvgIcon8 className={classes.icon9} />
              </div>
              <div className={classes.ofertaDoDia}>oferta do dia</div>
            </div>
          </div>
        </div>
      </div>
      <div className={classes.divDepartmentMenuV2__Container}>
        <div className={classes.main2}>
          <div className={classes.divDepartmentMenuV2__MenuWrapp}>
            <div className={classes.divDepartmentMenuV2__ButtonWra}>
              <div className={classes.sVG9}>
                <SvgIcon9 className={classes.icon10} />
              </div>
              <div className={classes.button4}>
                <div className={classes.todosOsDepartamentos}>todos os departamentos</div>
              </div>
              <div className={classes.sVG10}>
                <SvgIcon10 className={classes.icon11} />
              </div>
            </div>
          </div>
          <div className={classes.divMenuTrendingDepartments__Li}>
            <div className={classes.spanTrendingDepartmentsItemWit}>
              <div className={classes.linkMercado}>mercado</div>
            </div>
            <div className={classes.spanTrendingDepartmentsItemWit2}>
              <div className={classes.linkCelulares}>celulares</div>
            </div>
            <div className={classes.spanTrendingDepartmentsItemWit3}>
              <div className={classes.linkEletrodomesticos}>eletrodomésticos</div>
            </div>
            <div className={classes.spanTrendingDepartmentsItemWit4}>
              <div className={classes.linkInformatica}>informática</div>
            </div>
            <div className={classes.spanTrendingDepartmentsItemWit5}>
              <div className={classes.linkTvEHomeTheater}>tv e home theater</div>
            </div>
            <div className={classes.spanTrendingDepartmentsItemWit6}>
              <div className={classes.linkEletroportateis}>eletroportáteis</div>
            </div>
            <div className={classes.spanTrendingDepartmentsItemWit7}>
              <div className={classes.linkMoveis}>móveis</div>
            </div>
            <div className={classes.spanTrendingDepartmentsItemWit8}>
              <div className={classes.linkOutlet}>outlet</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
});

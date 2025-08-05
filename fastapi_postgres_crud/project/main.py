from datetime import datetime

from fastapi import FastAPI, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import SessionLocal
from models import (
    MasterDetails,
    BasicDetails,
    MinBasic,
    MaxBasic,
    TaxRebate,
    OldRegimeTaxSlabs,
    NewRegimeTaxSlabs,
    OldRegimeSurchargeSlabs,
    NewRegimeSurchargeSlabs,
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def parse_date(date_str: str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")


@app.get("/")
def read_root(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "master_list": db.query(MasterDetails).all(),
            "basic_list": db.query(BasicDetails).all(),
            "min_list": db.query(MinBasic).all(),
            "max_list": db.query(MaxBasic).all(),
            "rebate_list": db.query(TaxRebate).all(),
            "old_tax_list": db.query(OldRegimeTaxSlabs).all(),
            "new_tax_list": db.query(NewRegimeTaxSlabs).all(),
            "old_surcharge_list": db.query(OldRegimeSurchargeSlabs).all(),
            "new_surcharge_list": db.query(NewRegimeSurchargeSlabs).all(),
        },
    )


#
# MasterDetails CRUD
#
@app.post("/master/create")
def create_master(
        name: str = Form(...),
        company_id: str = Form(...),
        date_from: str = Form(...),
        date_to: str = Form(...),
        db: Session = Depends(get_db),
):
    md = MasterDetails(
        name=name,
        company_id=company_id,
        date_from=parse_date(date_from),
        date_to=parse_date(date_to),
    )
    db.add(md)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/master/update/{id}")
def update_master(
        id: int,
        name: str = Form(...),
        company_id: str = Form(...),
        date_from: str = Form(...),
        date_to: str = Form(...),
        db: Session = Depends(get_db),
):
    md = db.query(MasterDetails).get(id)
    if not md:
        raise HTTPException(404, "MasterDetails not found")
    md.name = name
    md.company_id = company_id
    md.date_from = parse_date(date_from)
    md.date_to = parse_date(date_to)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/master/delete/{id}")
def delete_master(id: int, db: Session = Depends(get_db)):
    md = db.query(MasterDetails).get(id)
    if not md:
        raise HTTPException(404, "MasterDetails not found")
    db.delete(md)
    db.commit()
    return RedirectResponse("/", status_code=303)


#
# BasicDetails CRUD
#
@app.post("/basic/create")
def create_basic(
        master_details_id: int = Form(...),
        basic_percentage: float = Form(...),
        hra: float = Form(...),
        stan_ded_old_regime: int = Form(...),
        stan_ded_new_regime: int = Form(...),
        gratuity_percentage: float = Form(...),
        gratuity_multiplier: float = Form(...),
        cess: float = Form(...),
        professional_tax: int = Form(...),
        physically_challenged: bool = Form(False),
        age_above: int = Form(...),
        monthly_salary_limit: int = Form(...),
        tax_deducted_at_source: float = Form(...),
        pf_percentage: float = Form(...),
        pf_ceiling_limit: float = Form(...),
        esic_ee_percentage: float = Form(...),
        esic_er_percentage: float = Form(...),
        esic_wage_limit: float = Form(...),
        esic_wag_lim_phy_cha: float = Form(...),
        db: Session = Depends(get_db),
):
    bd = BasicDetails(
        master_details_id=master_details_id,
        basic_percentage=basic_percentage,
        hra=hra,
        stan_ded_old_regime=stan_ded_old_regime,
        stan_ded_new_regime=stan_ded_new_regime,
        gratuity_percentage=gratuity_percentage,
        gratuity_multiplier=gratuity_multiplier,
        cess=cess,
        professional_tax=professional_tax,
        physically_challenged=physically_challenged,
        age_above=age_above,
        monthly_salary_limit=monthly_salary_limit,
        tax_deducted_at_source=tax_deducted_at_source,
        pf_percentage=pf_percentage,
        pf_ceiling_limit=pf_ceiling_limit,
        esic_ee_percentage=esic_ee_percentage,
        esic_er_percentage=esic_er_percentage,
        esic_wage_limit=esic_wage_limit,
        esic_wag_lim_phy_cha=esic_wag_lim_phy_cha,
    )
    db.add(bd)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/basic/update/{id}")
def update_basic(
        id: int,
        hra: float = Form(...),
        basic_percentage: float = Form(...),
        stan_ded_old_regime: int = Form(...),
        stan_ded_new_regime: int = Form(...),
        gratuity_percentage: float = Form(...),
        gratuity_multiplier: float = Form(...),
        cess: float = Form(...),
        professional_tax: int = Form(...),
        physically_challenged: bool = Form(False),
        age_above: int = Form(...),
        monthly_salary_limit: int = Form(...),
        tax_deducted_at_source: float = Form(...),
        pf_percentage: float = Form(...),
        pf_ceiling_limit: float = Form(...),
        esic_ee_percentage: float = Form(...),
        esic_er_percentage: float = Form(...),
        esic_wage_limit: float = Form(...),
        esic_wag_lim_phy_cha: float = Form(...),
        db: Session = Depends(get_db),
):
    bd = db.query(BasicDetails).get(id)
    if not bd:
        raise HTTPException(404, "BasicDetails not found")
    bd.hra = hra
    bd.basic_percentage = basic_percentage
    bd.stan_ded_old_regime = stan_ded_old_regime
    bd.stan_ded_new_regime = stan_ded_new_regime
    bd.gratuity_percentage = gratuity_percentage
    bd.gratuity_multiplier = gratuity_multiplier
    bd.cess = cess
    bd.professional_tax = professional_tax
    bd.physically_challenged = physically_challenged
    bd.age_above = age_above
    bd.monthly_salary_limit = monthly_salary_limit
    bd.tax_deducted_at_source = tax_deducted_at_source
    bd.pf_percentage = pf_percentage
    bd.pf_ceiling_limit = pf_ceiling_limit
    bd.esic_ee_percentage = esic_ee_percentage
    bd.esic_er_percentage = esic_er_percentage
    bd.esic_wage_limit = esic_wage_limit
    bd.esic_wag_lim_phy_cha = esic_wag_lim_phy_cha
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/basic/delete/{id}")
def delete_basic(id: int, db: Session = Depends(get_db)):
    bd = db.query(BasicDetails).get(id)
    if not bd:
        raise HTTPException(404, "BasicDetails not found")
    db.delete(bd)
    db.commit()
    return RedirectResponse("/", status_code=303)


#
# MinBasic CRUD
#
@app.post("/minbasic/create")
def create_minbasic(
        master_details_id: int = Form(...),
        date_from: str = Form(...),
        date_to: str = Form(...),
        amount: float = Form(...),
        db: Session = Depends(get_db),
):
    mb = MinBasic(
        master_details_id=master_details_id,
        date_from=parse_date(date_from),
        date_to=parse_date(date_to),
        amount=amount,
    )
    db.add(mb)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/minbasic/update/{id}")
def update_minbasic(
        id: int,
        date_from: str = Form(...),
        date_to: str = Form(...),
        amount: float = Form(...),
        db: Session = Depends(get_db),
):
    mb = db.query(MinBasic).get(id)
    if not mb:
        raise HTTPException(404, "MinBasic not found")
    mb.date_from = parse_date(date_from)
    mb.date_to = parse_date(date_to)
    mb.amount = amount
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/minbasic/delete/{id}")
def delete_minbasic(id: int, db: Session = Depends(get_db)):
    mb = db.query(MinBasic).get(id)
    if not mb:
        raise HTTPException(404, "MinBasic not found")
    db.delete(mb)
    db.commit()
    return RedirectResponse("/", status_code=303)


#
# MaxBasic CRUD
#
@app.post("/maxbasic/create")
def create_maxbasic(
        master_details_id: int = Form(...),
        date_from: str = Form(...),
        date_to: str = Form(...),
        amount: float = Form(...),
        db: Session = Depends(get_db),
):
    xb = MaxBasic(
        master_details_id=master_details_id,
        date_from=parse_date(date_from),
        date_to=parse_date(date_to),
        amount=amount,
    )
    db.add(xb)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/maxbasic/update/{id}")
def update_maxbasic(
        id: int,
        date_from: str = Form(...),
        date_to: str = Form(...),
        amount: float = Form(...),
        db: Session = Depends(get_db),
):
    xb = db.query(MaxBasic).get(id)
    if not xb:
        raise HTTPException(404, "MaxBasic not found")
    xb.date_from = parse_date(date_from)
    xb.date_to = parse_date(date_to)
    xb.amount = amount
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/maxbasic/delete/{id}")
def delete_maxbasic(id: int, db: Session = Depends(get_db)):
    xb = db.query(MaxBasic).get(id)
    if not xb:
        raise HTTPException(404, "MaxBasic not found")
    db.delete(xb)
    db.commit()
    return RedirectResponse("/", status_code=303)


# TaxRebate CRUD
@app.post("/rebate/create")
def create_rebate(
        master_details_id: int = Form(...),
        old_tax_nor_cit_reba_amo: float = Form(...),
        old_tax_nor_cit_reba_inc: float = Form(...),
        old_tax_sen_cit_reba_amo: float = Form(...),
        old_tax_sen_cit_reba_inc: float = Form(...),
        old_tax_sup_sen_cit_reba_amo: float = Form(...),
        old_tax_sup_sen_cit_reba_inc: float = Form(...),
        new_tax_nor_cit_reba_amo: float = Form(...),
        new_tax_nor_cit_reba_inc: float = Form(...),
        new_tax_sen_cit_reba_amo: float = Form(...),
        new_tax_sen_cit_reba_inc: float = Form(...),
        new_tax_sup_sen_cit_reba_amo: float = Form(...),
        new_tax_sup_sen_cit_reba_inc: float = Form(...),
        db: Session = Depends(get_db),
):
    tr = TaxRebate(
        master_details_id=master_details_id,
        old_tax_nor_cit_reba_amo=old_tax_nor_cit_reba_amo,
        old_tax_nor_cit_reba_inc=old_tax_nor_cit_reba_inc,
        old_tax_sen_cit_reba_amo=old_tax_sen_cit_reba_amo,
        old_tax_sen_cit_reba_inc=old_tax_sen_cit_reba_inc,
        old_tax_sup_sen_cit_reba_amo=old_tax_sup_sen_cit_reba_amo,
        old_tax_sup_sen_cit_reba_inc=old_tax_sup_sen_cit_reba_inc,
        new_tax_nor_cit_reba_amo=new_tax_nor_cit_reba_amo,
        new_tax_nor_cit_reba_inc=new_tax_nor_cit_reba_inc,
        new_tax_sen_cit_reba_amo=new_tax_sen_cit_reba_amo,
        new_tax_sen_cit_reba_inc=new_tax_sen_cit_reba_inc,
        new_tax_sup_sen_cit_reba_amo=new_tax_sup_sen_cit_reba_amo,
        new_tax_sup_sen_cit_reba_inc=new_tax_sup_sen_cit_reba_inc,
    )
    db.add(tr)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/rebate/update/{id}")
def update_rebate(
        id: int,
        old_tax_nor_cit_reba_amo: float = Form(...),
        old_tax_nor_cit_reba_inc: float = Form(...),
        old_tax_sen_cit_reba_amo: float = Form(...),
        old_tax_sen_cit_reba_inc: float = Form(...),
        old_tax_sup_sen_cit_reba_amo: float = Form(...),
        old_tax_sup_sen_cit_reba_inc: float = Form(...),
        new_tax_nor_cit_reba_amo: float = Form(...),
        new_tax_nor_cit_reba_inc: float = Form(...),
        new_tax_sen_cit_reba_amo: float = Form(...),
        new_tax_sen_cit_reba_inc: float = Form(...),
        new_tax_sup_sen_cit_reba_amo: float = Form(...),
        new_tax_sup_sen_cit_reba_inc: float = Form(...),
        db: Session = Depends(get_db),
):
    tr = db.query(TaxRebate).get(id)
    if not tr:
        raise HTTPException(404, "TaxRebate not found")
    tr.old_tax_nor_cit_reba_amo = old_tax_nor_cit_reba_amo
    tr.old_tax_nor_cit_reba_inc = old_tax_nor_cit_reba_inc
    tr.old_tax_sen_cit_reba_amo = old_tax_sen_cit_reba_amo
    tr.old_tax_sen_cit_reba_inc = old_tax_sen_cit_reba_inc
    tr.old_tax_sup_sen_cit_reba_amo = old_tax_sup_sen_cit_reba_amo
    tr.old_tax_sup_sen_cit_reba_inc = old_tax_sup_sen_cit_reba_inc
    tr.new_tax_nor_cit_reba_amo = new_tax_nor_cit_reba_amo
    tr.new_tax_nor_cit_reba_inc = new_tax_nor_cit_reba_inc
    tr.new_tax_sen_cit_reba_amo = new_tax_sen_cit_reba_amo
    tr.new_tax_sen_cit_reba_inc = new_tax_sen_cit_reba_inc
    tr.new_tax_sup_sen_cit_reba_amo = new_tax_sup_sen_cit_reba_amo
    tr.new_tax_sup_sen_cit_reba_inc = new_tax_sup_sen_cit_reba_inc
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/rebate/delete/{id}")
def delete_rebate(id: int, db: Session = Depends(get_db)):
    tr = db.query(TaxRebate).get(id)
    if not tr:
        raise HTTPException(404, "TaxRebate not found")
    db.delete(tr)
    db.commit()
    return RedirectResponse("/", status_code=303)


# OldRegimeTaxSlabs CRUD
@app.post("/oldtax/create")
def create_oldtax(
        master_details_id: int = Form(...),
        amount_from: int = Form(...),
        amount_to: int = Form(...),
        normal_citizen_percentage: float = Form(...),
        senior_citizen_percentage: float = Form(...),
        super_senior_citizen_percentage: float = Form(...),
        db: Session = Depends(get_db),
):
    ot = OldRegimeTaxSlabs(
        master_details_id=master_details_id,
        amount_from=amount_from,
        amount_to=amount_to,
        normal_citizen_percentage=normal_citizen_percentage,
        senior_citizen_percentage=senior_citizen_percentage,
        super_senior_citizen_percentage=super_senior_citizen_percentage,
    )
    db.add(ot)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/oldtax/update/{id}")
def update_oldtax(
        id: int,
        amount_from: int = Form(...),
        amount_to: int = Form(...),
        normal_citizen_percentage: float = Form(...),
        senior_citizen_percentage: float = Form(...),
        super_senior_citizen_percentage: float = Form(...),
        db: Session = Depends(get_db),
):
    ot = db.query(OldRegimeTaxSlabs).get(id)
    if not ot:
        raise HTTPException(404, "OldRegimeTaxSlabs not found")
    ot.amount_from = amount_from
    ot.amount_to = amount_to
    ot.normal_citizen_percentage = normal_citizen_percentage
    ot.senior_citizen_percentage = senior_citizen_percentage
    ot.super_senior_citizen_percentage = super_senior_citizen_percentage
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/oldtax/delete/{id}")
def delete_oldtax(id: int, db: Session = Depends(get_db)):
    ot = db.query(OldRegimeTaxSlabs).get(id)
    if not ot:
        raise HTTPException(404, "OldRegimeTaxSlabs not found")
    db.delete(ot)
    db.commit()
    return RedirectResponse("/", status_code=303)


# NewRegimeTaxSlabs CRUD
@app.post("/newtax/create")
def create_newtax(
        master_details_id: int = Form(...),
        amount_from: int = Form(...),
        amount_to: int = Form(...),
        normal_citizen_percentage: float = Form(...),
        senior_citizen_percentage: float = Form(...),
        super_senior_citizen_percentage: float = Form(...),
        db: Session = Depends(get_db),
):
    nt = NewRegimeTaxSlabs(
        master_details_id=master_details_id,
        amount_from=amount_from,
        amount_to=amount_to,
        normal_citizen_percentage=normal_citizen_percentage,
        senior_citizen_percentage=senior_citizen_percentage,
        super_senior_citizen_percentage=super_senior_citizen_percentage,
    )
    db.add(nt)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/newtax/update/{id}")
def update_newtax(
        id: int,
        amount_from: int = Form(...),
        amount_to: int = Form(...),
        normal_citizen_percentage: float = Form(...),
        senior_citizen_percentage: float = Form(...),
        super_senior_citizen_percentage: float = Form(...),
        db: Session = Depends(get_db),
):
    nt = db.query(NewRegimeTaxSlabs).get(id)
    if not nt:
        raise HTTPException(404, "NewRegimeTaxSlabs not found")
    nt.amount_from = amount_from
    nt.amount_to = amount_to
    nt.normal_citizen_percentage = normal_citizen_percentage
    nt.senior_citizen_percentage = senior_citizen_percentage
    nt.super_senior_citizen_percentage = super_senior_citizen_percentage
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/newtax/delete/{id}")
def delete_newtax(id: int, db: Session = Depends(get_db)):
    nt = db.query(NewRegimeTaxSlabs).get(id)
    if not nt:
        raise HTTPException(404, "NewRegimeTaxSlabs not found")
    db.delete(nt)
    db.commit()
    return RedirectResponse("/", status_code=303)


# OldRegimeSurchargeSlabs CRUD
@app.post("/oldsurcharge/create")
def create_oldsurcharge(
        master_details_id: int = Form(...),
        amount_from: int = Form(...),
        amount_to: int = Form(...),
        normal_citizen_percentage: float = Form(...),
        senior_citizen_percentage: float = Form(...),
        super_senior_citizen_percentage: float = Form(...),
        db: Session = Depends(get_db),
):
    osl = OldRegimeSurchargeSlabs(
        master_details_id=master_details_id,
        amount_from=amount_from,
        amount_to=amount_to,
        normal_citizen_percentage=normal_citizen_percentage,
        senior_citizen_percentage=senior_citizen_percentage,
        super_senior_citizen_percentage=super_senior_citizen_percentage,
    )
    db.add(osl)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/oldsurcharge/update/{id}")
def update_oldsurcharge(
        id: int,
        amount_from: int = Form(...),
        amount_to: int = Form(...),
        normal_citizen_percentage: float = Form(...),
        senior_citizen_percentage: float = Form(...),
        super_senior_citizen_percentage: float = Form(...),
        db: Session = Depends(get_db),
):
    osl = db.query(OldRegimeSurchargeSlabs).get(id)
    if not osl:
        raise HTTPException(404, "OldRegimeSurchargeSlabs not found")
    osl.amount_from = amount_from
    osl.amount_to = amount_to
    osl.normal_citizen_percentage = normal_citizen_percentage
    osl.senior_citizen_percentage = senior_citizen_percentage
    osl.super_senior_citizen_percentage = super_senior_citizen_percentage
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/oldsurcharge/delete/{id}")
def delete_oldsurcharge(id: int, db: Session = Depends(get_db)):
    osl = db.query(OldRegimeSurchargeSlabs).get(id)
    if not osl:
        raise HTTPException(404, "OldRegimeSurchargeSlabs not found")
    db.delete(osl)
    db.commit()
    return RedirectResponse("/", status_code=303)


# NewRegimeSurchargeSlabs CRUD
@app.post("/newsurcharge/create")
def create_newsurcharge(
        master_details_id: int = Form(...),
        amount_from: int = Form(...),
        amount_to: int = Form(...),
        normal_citizen_percentage: float = Form(...),
        senior_citizen_percentage: float = Form(...),
        super_senior_citizen_percentage: float = Form(...),
        db: Session = Depends(get_db),
):
    nsl = NewRegimeSurchargeSlabs(
        master_details_id=master_details_id,
        amount_from=amount_from,
        amount_to=amount_to,
        normal_citizen_percentage=normal_citizen_percentage,
        senior_citizen_percentage=senior_citizen_percentage,
        super_senior_citizen_percentage=super_senior_citizen_percentage,
    )
    db.add(nsl)
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/newsurcharge/update/{id}")
def update_newsurcharge(
        id: int,
        amount_from: int = Form(...),
        amount_to: int = Form(...),
        normal_citizen_percentage: float = Form(...),
        senior_citizen_percentage: float = Form(...),
        super_senior_citizen_percentage: float = Form(...),
        db: Session = Depends(get_db),
):
    nsl = db.query(NewRegimeSurchargeSlabs).get(id)
    if not nsl:
        raise HTTPException(404, "NewRegimeSurchargeSlabs not found")
    nsl.amount_from = amount_from
    nsl.amount_to = amount_to
    nsl.normal_citizen_percentage = normal_citizen_percentage
    nsl.senior_citizen_percentage = senior_citizen_percentage
    nsl.super_senior_citizen_percentage = super_senior_citizen_percentage
    db.commit()
    return RedirectResponse("/", status_code=303)


@app.post("/newsurcharge/delete/{id}")
def delete_newsurcharge(id: int, db: Session = Depends(get_db)):
    nsl = db.query(NewRegimeSurchargeSlabs).get(id)
    if not nsl:
        raise HTTPException(404, "NewRegimeSurchargeSlabs not found")
    db.delete(nsl)
    db.commit()
    return RedirectResponse("/", status_code=303)

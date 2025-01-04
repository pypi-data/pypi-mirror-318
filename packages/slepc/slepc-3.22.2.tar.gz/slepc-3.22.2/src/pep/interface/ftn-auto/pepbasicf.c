#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* pepbasic.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcpep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepcreate_ PEPCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepcreate_ pepcreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsettype_ PEPSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsettype_ pepsettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgettype_ PEPGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgettype_ pepgettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepreset_ PEPRESET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepreset_ pepreset
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepdestroy_ PEPDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepdestroy_ pepdestroy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetbv_ PEPSETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetbv_ pepsetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetbv_ PEPGETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetbv_ pepgetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetrg_ PEPSETRG
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetrg_ pepsetrg
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetrg_ PEPGETRG
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetrg_ pepgetrg
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetds_ PEPSETDS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetds_ pepsetds
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetds_ PEPGETDS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetds_ pepgetds
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetst_ PEPSETST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetst_ pepsetst
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetst_ PEPGETST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetst_ pepgetst
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define peprefinegetksp_ PEPREFINEGETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define peprefinegetksp_ peprefinegetksp
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsettarget_ PEPSETTARGET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsettarget_ pepsettarget
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgettarget_ PEPGETTARGET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgettarget_ pepgettarget
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetinterval_ PEPSETINTERVAL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetinterval_ pepsetinterval
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetinterval_ PEPGETINTERVAL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetinterval_ pepgetinterval
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  pepcreate_(MPI_Fint * comm,PEP *outpep, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(outpep);
 PetscBool outpep_null = !*(void**) outpep ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(outpep);
*ierr = PEPCreate(
	MPI_Comm_f2c(*(comm)),outpep);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! outpep_null && !*(void**) outpep) * (void **) outpep = (void *)-2;
}
SLEPC_EXTERN void  pepsettype_(PEP pep,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(pep);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = PEPSetType(
	(PEP)PetscToPointer((pep) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  pepgettype_(PEP pep,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPGetType(
	(PEP)PetscToPointer((pep) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  pepreset_(PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPReset(
	(PEP)PetscToPointer((pep) ));
}
SLEPC_EXTERN void  pepdestroy_(PEP *pep, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(pep);
 PetscBool pep_null = !*(void**) pep ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPDestroy(pep);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! pep_null && !*(void**) pep) * (void **) pep = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(pep);
 }
SLEPC_EXTERN void  pepsetbv_(PEP pep,BV bv, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(bv);
*ierr = PEPSetBV(
	(PEP)PetscToPointer((pep) ),
	(BV)PetscToPointer((bv) ));
}
SLEPC_EXTERN void  pepgetbv_(PEP pep,BV *bv, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
PetscBool bv_null = !*(void**) bv ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(bv);
*ierr = PEPGetBV(
	(PEP)PetscToPointer((pep) ),bv);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! bv_null && !*(void**) bv) * (void **) bv = (void *)-2;
}
SLEPC_EXTERN void  pepsetrg_(PEP pep,RG rg, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(rg);
*ierr = PEPSetRG(
	(PEP)PetscToPointer((pep) ),
	(RG)PetscToPointer((rg) ));
}
SLEPC_EXTERN void  pepgetrg_(PEP pep,RG *rg, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
PetscBool rg_null = !*(void**) rg ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(rg);
*ierr = PEPGetRG(
	(PEP)PetscToPointer((pep) ),rg);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! rg_null && !*(void**) rg) * (void **) rg = (void *)-2;
}
SLEPC_EXTERN void  pepsetds_(PEP pep,DS ds, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(ds);
*ierr = PEPSetDS(
	(PEP)PetscToPointer((pep) ),
	(DS)PetscToPointer((ds) ));
}
SLEPC_EXTERN void  pepgetds_(PEP pep,DS *ds, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
PetscBool ds_null = !*(void**) ds ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ds);
*ierr = PEPGetDS(
	(PEP)PetscToPointer((pep) ),ds);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ds_null && !*(void**) ds) * (void **) ds = (void *)-2;
}
SLEPC_EXTERN void  pepsetst_(PEP pep,ST st, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLOBJECT(st);
*ierr = PEPSetST(
	(PEP)PetscToPointer((pep) ),
	(ST)PetscToPointer((st) ));
}
SLEPC_EXTERN void  pepgetst_(PEP pep,ST *st, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
PetscBool st_null = !*(void**) st ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(st);
*ierr = PEPGetST(
	(PEP)PetscToPointer((pep) ),st);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! st_null && !*(void**) st) * (void **) st = (void *)-2;
}
SLEPC_EXTERN void  peprefinegetksp_(PEP pep,KSP *ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
PetscBool ksp_null = !*(void**) ksp ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ksp);
*ierr = PEPRefineGetKSP(
	(PEP)PetscToPointer((pep) ),ksp);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ksp_null && !*(void**) ksp) * (void **) ksp = (void *)-2;
}
SLEPC_EXTERN void  pepsettarget_(PEP pep,PetscScalar *target, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetTarget(
	(PEP)PetscToPointer((pep) ),*target);
}
SLEPC_EXTERN void  pepgettarget_(PEP pep,PetscScalar* target, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLSCALAR(target);
*ierr = PEPGetTarget(
	(PEP)PetscToPointer((pep) ),target);
}
SLEPC_EXTERN void  pepsetinterval_(PEP pep,PetscReal *inta,PetscReal *intb, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetInterval(
	(PEP)PetscToPointer((pep) ),*inta,*intb);
}
SLEPC_EXTERN void  pepgetinterval_(PEP pep,PetscReal* inta,PetscReal* intb, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLREAL(inta);
CHKFORTRANNULLREAL(intb);
*ierr = PEPGetInterval(
	(PEP)PetscToPointer((pep) ),inta,intb);
}
#if defined(__cplusplus)
}
#endif

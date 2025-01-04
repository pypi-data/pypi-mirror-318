#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* epsbasic.c */
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

#include "slepceps.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epscreate_ EPSCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epscreate_ epscreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssettype_ EPSSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssettype_ epssettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsgettype_ EPSGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsgettype_ epsgettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsreset_ EPSRESET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsreset_ epsreset
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsdestroy_ EPSDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsdestroy_ epsdestroy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssettarget_ EPSSETTARGET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssettarget_ epssettarget
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsgettarget_ EPSGETTARGET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsgettarget_ epsgettarget
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetinterval_ EPSSETINTERVAL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetinterval_ epssetinterval
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsgetinterval_ EPSGETINTERVAL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsgetinterval_ epsgetinterval
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetst_ EPSSETST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetst_ epssetst
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsgetst_ EPSGETST
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsgetst_ epsgetst
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetbv_ EPSSETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetbv_ epssetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsgetbv_ EPSGETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsgetbv_ epsgetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetrg_ EPSSETRG
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetrg_ epssetrg
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsgetrg_ EPSGETRG
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsgetrg_ epsgetrg
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epssetds_ EPSSETDS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epssetds_ epssetds
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsgetds_ EPSGETDS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsgetds_ epsgetds
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsisgeneralized_ EPSISGENERALIZED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsisgeneralized_ epsisgeneralized
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsishermitian_ EPSISHERMITIAN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsishermitian_ epsishermitian
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsispositive_ EPSISPOSITIVE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsispositive_ epsispositive
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epsisstructured_ EPSISSTRUCTURED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epsisstructured_ epsisstructured
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  epscreate_(MPI_Fint * comm,EPS *outeps, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(outeps);
 PetscBool outeps_null = !*(void**) outeps ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(outeps);
*ierr = EPSCreate(
	MPI_Comm_f2c(*(comm)),outeps);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! outeps_null && !*(void**) outeps) * (void **) outeps = (void *)-2;
}
SLEPC_EXTERN void  epssettype_(EPS eps,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(eps);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = EPSSetType(
	(EPS)PetscToPointer((eps) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  epsgettype_(EPS eps,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSGetType(
	(EPS)PetscToPointer((eps) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  epsreset_(EPS eps, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSReset(
	(EPS)PetscToPointer((eps) ));
}
SLEPC_EXTERN void  epsdestroy_(EPS *eps, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(eps);
 PetscBool eps_null = !*(void**) eps ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSDestroy(eps);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! eps_null && !*(void**) eps) * (void **) eps = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(eps);
 }
SLEPC_EXTERN void  epssettarget_(EPS eps,PetscScalar *target, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSSetTarget(
	(EPS)PetscToPointer((eps) ),*target);
}
SLEPC_EXTERN void  epsgettarget_(EPS eps,PetscScalar* target, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLSCALAR(target);
*ierr = EPSGetTarget(
	(EPS)PetscToPointer((eps) ),target);
}
SLEPC_EXTERN void  epssetinterval_(EPS eps,PetscReal *inta,PetscReal *intb, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSSetInterval(
	(EPS)PetscToPointer((eps) ),*inta,*intb);
}
SLEPC_EXTERN void  epsgetinterval_(EPS eps,PetscReal* inta,PetscReal* intb, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLREAL(inta);
CHKFORTRANNULLREAL(intb);
*ierr = EPSGetInterval(
	(EPS)PetscToPointer((eps) ),inta,intb);
}
SLEPC_EXTERN void  epssetst_(EPS eps,ST st, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(st);
*ierr = EPSSetST(
	(EPS)PetscToPointer((eps) ),
	(ST)PetscToPointer((st) ));
}
SLEPC_EXTERN void  epsgetst_(EPS eps,ST *st, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool st_null = !*(void**) st ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(st);
*ierr = EPSGetST(
	(EPS)PetscToPointer((eps) ),st);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! st_null && !*(void**) st) * (void **) st = (void *)-2;
}
SLEPC_EXTERN void  epssetbv_(EPS eps,BV V, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(V);
*ierr = EPSSetBV(
	(EPS)PetscToPointer((eps) ),
	(BV)PetscToPointer((V) ));
}
SLEPC_EXTERN void  epsgetbv_(EPS eps,BV *V, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool V_null = !*(void**) V ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(V);
*ierr = EPSGetBV(
	(EPS)PetscToPointer((eps) ),V);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! V_null && !*(void**) V) * (void **) V = (void *)-2;
}
SLEPC_EXTERN void  epssetrg_(EPS eps,RG rg, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(rg);
*ierr = EPSSetRG(
	(EPS)PetscToPointer((eps) ),
	(RG)PetscToPointer((rg) ));
}
SLEPC_EXTERN void  epsgetrg_(EPS eps,RG *rg, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool rg_null = !*(void**) rg ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(rg);
*ierr = EPSGetRG(
	(EPS)PetscToPointer((eps) ),rg);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! rg_null && !*(void**) rg) * (void **) rg = (void *)-2;
}
SLEPC_EXTERN void  epssetds_(EPS eps,DS ds, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(ds);
*ierr = EPSSetDS(
	(EPS)PetscToPointer((eps) ),
	(DS)PetscToPointer((ds) ));
}
SLEPC_EXTERN void  epsgetds_(EPS eps,DS *ds, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool ds_null = !*(void**) ds ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ds);
*ierr = EPSGetDS(
	(EPS)PetscToPointer((eps) ),ds);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ds_null && !*(void**) ds) * (void **) ds = (void *)-2;
}
SLEPC_EXTERN void  epsisgeneralized_(EPS eps,PetscBool* is, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSIsGeneralized(
	(EPS)PetscToPointer((eps) ),is);
}
SLEPC_EXTERN void  epsishermitian_(EPS eps,PetscBool* is, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSIsHermitian(
	(EPS)PetscToPointer((eps) ),is);
}
SLEPC_EXTERN void  epsispositive_(EPS eps,PetscBool* is, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSIsPositive(
	(EPS)PetscToPointer((eps) ),is);
}
SLEPC_EXTERN void  epsisstructured_(EPS eps,PetscBool* is, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSIsStructured(
	(EPS)PetscToPointer((eps) ),is);
}
#if defined(__cplusplus)
}
#endif

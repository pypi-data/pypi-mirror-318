#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* lmebasic.c */
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

#include "slepclme.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmeview_ LMEVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmeview_ lmeview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmeviewfromoptions_ LMEVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmeviewfromoptions_ lmeviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmeconvergedreasonview_ LMECONVERGEDREASONVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmeconvergedreasonview_ lmeconvergedreasonview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmeconvergedreasonviewfromoptions_ LMECONVERGEDREASONVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmeconvergedreasonviewfromoptions_ lmeconvergedreasonviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmecreate_ LMECREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmecreate_ lmecreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesettype_ LMESETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesettype_ lmesettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegettype_ LMEGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegettype_ lmegettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmereset_ LMERESET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmereset_ lmereset
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmedestroy_ LMEDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmedestroy_ lmedestroy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesetbv_ LMESETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetbv_ lmesetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetbv_ LMEGETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetbv_ lmegetbv
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  lmeview_(LME lme,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLOBJECT(viewer);
*ierr = LMEView(
	(LME)PetscToPointer((lme) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  lmeviewfromoptions_(LME lme,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = LMEViewFromOptions(
	(LME)PetscToPointer((lme) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  lmeconvergedreasonview_(LME lme,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLOBJECT(viewer);
*ierr = LMEConvergedReasonView(
	(LME)PetscToPointer((lme) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  lmeconvergedreasonviewfromoptions_(LME lme, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEConvergedReasonViewFromOptions(
	(LME)PetscToPointer((lme) ));
}
SLEPC_EXTERN void  lmecreate_(MPI_Fint * comm,LME *outlme, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(outlme);
 PetscBool outlme_null = !*(void**) outlme ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(outlme);
*ierr = LMECreate(
	MPI_Comm_f2c(*(comm)),outlme);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! outlme_null && !*(void**) outlme) * (void **) outlme = (void *)-2;
}
SLEPC_EXTERN void  lmesettype_(LME lme,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(lme);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = LMESetType(
	(LME)PetscToPointer((lme) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  lmegettype_(LME lme,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEGetType(
	(LME)PetscToPointer((lme) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  lmereset_(LME lme, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEReset(
	(LME)PetscToPointer((lme) ));
}
SLEPC_EXTERN void  lmedestroy_(LME *lme, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(lme);
 PetscBool lme_null = !*(void**) lme ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEDestroy(lme);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! lme_null && !*(void**) lme) * (void **) lme = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(lme);
 }
SLEPC_EXTERN void  lmesetbv_(LME lme,BV bv, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLOBJECT(bv);
*ierr = LMESetBV(
	(LME)PetscToPointer((lme) ),
	(BV)PetscToPointer((bv) ));
}
SLEPC_EXTERN void  lmegetbv_(LME lme,BV *bv, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
PetscBool bv_null = !*(void**) bv ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(bv);
*ierr = LMEGetBV(
	(LME)PetscToPointer((lme) ),bv);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! bv_null && !*(void**) bv) * (void **) bv = (void *)-2;
}
#if defined(__cplusplus)
}
#endif

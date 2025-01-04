#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* lmeopts.c */
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
#define lmesetfromoptions_ LMESETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetfromoptions_ lmesetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesetproblemtype_ LMESETPROBLEMTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetproblemtype_ lmesetproblemtype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetproblemtype_ LMEGETPROBLEMTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetproblemtype_ lmegetproblemtype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegettolerances_ LMEGETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegettolerances_ lmegettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesettolerances_ LMESETTOLERANCES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesettolerances_ lmesettolerances
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetdimensions_ LMEGETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetdimensions_ lmegetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesetdimensions_ LMESETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetdimensions_ lmesetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmeseterrorifnotconverged_ LMESETERRORIFNOTCONVERGED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmeseterrorifnotconverged_ lmeseterrorifnotconverged
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegeterrorifnotconverged_ LMEGETERRORIFNOTCONVERGED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegeterrorifnotconverged_ lmegeterrorifnotconverged
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesetoptionsprefix_ LMESETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetoptionsprefix_ lmesetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmeappendoptionsprefix_ LMEAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmeappendoptionsprefix_ lmeappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetoptionsprefix_ LMEGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetoptionsprefix_ lmegetoptionsprefix
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  lmesetfromoptions_(LME lme, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMESetFromOptions(
	(LME)PetscToPointer((lme) ));
}
SLEPC_EXTERN void  lmesetproblemtype_(LME lme,LMEProblemType *type, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMESetProblemType(
	(LME)PetscToPointer((lme) ),*type);
}
SLEPC_EXTERN void  lmegetproblemtype_(LME lme,LMEProblemType *type, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEGetProblemType(
	(LME)PetscToPointer((lme) ),type);
}
SLEPC_EXTERN void  lmegettolerances_(LME lme,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLREAL(tol);
CHKFORTRANNULLINTEGER(maxits);
*ierr = LMEGetTolerances(
	(LME)PetscToPointer((lme) ),tol,maxits);
}
SLEPC_EXTERN void  lmesettolerances_(LME lme,PetscReal *tol,PetscInt *maxits, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMESetTolerances(
	(LME)PetscToPointer((lme) ),*tol,*maxits);
}
SLEPC_EXTERN void  lmegetdimensions_(LME lme,PetscInt *ncv, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLINTEGER(ncv);
*ierr = LMEGetDimensions(
	(LME)PetscToPointer((lme) ),ncv);
}
SLEPC_EXTERN void  lmesetdimensions_(LME lme,PetscInt *ncv, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMESetDimensions(
	(LME)PetscToPointer((lme) ),*ncv);
}
SLEPC_EXTERN void  lmeseterrorifnotconverged_(LME lme,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMESetErrorIfNotConverged(
	(LME)PetscToPointer((lme) ),*flg);
}
SLEPC_EXTERN void  lmegeterrorifnotconverged_(LME lme,PetscBool *flag, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEGetErrorIfNotConverged(
	(LME)PetscToPointer((lme) ),flag);
}
SLEPC_EXTERN void  lmesetoptionsprefix_(LME lme, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(lme);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = LMESetOptionsPrefix(
	(LME)PetscToPointer((lme) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  lmeappendoptionsprefix_(LME lme, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(lme);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = LMEAppendOptionsPrefix(
	(LME)PetscToPointer((lme) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  lmegetoptionsprefix_(LME lme, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEGetOptionsPrefix(
	(LME)PetscToPointer((lme) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
#if defined(__cplusplus)
}
#endif

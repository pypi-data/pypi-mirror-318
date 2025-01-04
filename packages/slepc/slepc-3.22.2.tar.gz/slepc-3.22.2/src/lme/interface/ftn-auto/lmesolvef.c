#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* lmesolve.c */
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
#define lmesolve_ LMESOLVE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesolve_ lmesolve
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetiterationnumber_ LMEGETITERATIONNUMBER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetiterationnumber_ lmegetiterationnumber
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetconvergedreason_ LMEGETCONVERGEDREASON
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetconvergedreason_ lmegetconvergedreason
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegeterrorestimate_ LMEGETERRORESTIMATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegeterrorestimate_ lmegeterrorestimate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmecomputeerror_ LMECOMPUTEERROR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmecomputeerror_ lmecomputeerror
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  lmesolve_(LME lme, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMESolve(
	(LME)PetscToPointer((lme) ));
}
SLEPC_EXTERN void  lmegetiterationnumber_(LME lme,PetscInt *its, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLINTEGER(its);
*ierr = LMEGetIterationNumber(
	(LME)PetscToPointer((lme) ),its);
}
SLEPC_EXTERN void  lmegetconvergedreason_(LME lme,LMEConvergedReason *reason, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEGetConvergedReason(
	(LME)PetscToPointer((lme) ),reason);
}
SLEPC_EXTERN void  lmegeterrorestimate_(LME lme,PetscReal *errest, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLREAL(errest);
*ierr = LMEGetErrorEstimate(
	(LME)PetscToPointer((lme) ),errest);
}
SLEPC_EXTERN void  lmecomputeerror_(LME lme,PetscReal *error, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLREAL(error);
*ierr = LMEComputeError(
	(LME)PetscToPointer((lme) ),error);
}
#if defined(__cplusplus)
}
#endif

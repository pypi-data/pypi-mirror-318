#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* lmesetup.c */
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
#define lmesetup_ LMESETUP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetup_ lmesetup
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesetcoefficients_ LMESETCOEFFICIENTS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetcoefficients_ lmesetcoefficients
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetcoefficients_ LMEGETCOEFFICIENTS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetcoefficients_ lmegetcoefficients
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesetrhs_ LMESETRHS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetrhs_ lmesetrhs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetrhs_ LMEGETRHS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetrhs_ lmegetrhs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmesetsolution_ LMESETSOLUTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmesetsolution_ lmesetsolution
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmegetsolution_ LMEGETSOLUTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmegetsolution_ lmegetsolution
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define lmeallocatesolution_ LMEALLOCATESOLUTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define lmeallocatesolution_ lmeallocatesolution
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  lmesetup_(LME lme, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMESetUp(
	(LME)PetscToPointer((lme) ));
}
SLEPC_EXTERN void  lmesetcoefficients_(LME lme,Mat A,Mat B,Mat D,Mat E, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(B);
CHKFORTRANNULLOBJECT(D);
CHKFORTRANNULLOBJECT(E);
*ierr = LMESetCoefficients(
	(LME)PetscToPointer((lme) ),
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((B) ),
	(Mat)PetscToPointer((D) ),
	(Mat)PetscToPointer((E) ));
}
SLEPC_EXTERN void  lmegetcoefficients_(LME lme,Mat *A,Mat *B,Mat *D,Mat *E, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
PetscBool B_null = !*(void**) B ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(B);
PetscBool D_null = !*(void**) D ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(D);
PetscBool E_null = !*(void**) E ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(E);
*ierr = LMEGetCoefficients(
	(LME)PetscToPointer((lme) ),A,B,D,E);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! B_null && !*(void**) B) * (void **) B = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! D_null && !*(void**) D) * (void **) D = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! E_null && !*(void**) E) * (void **) E = (void *)-2;
}
SLEPC_EXTERN void  lmesetrhs_(LME lme,Mat C, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLOBJECT(C);
*ierr = LMESetRHS(
	(LME)PetscToPointer((lme) ),
	(Mat)PetscToPointer((C) ));
}
SLEPC_EXTERN void  lmegetrhs_(LME lme,Mat *C, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
PetscBool C_null = !*(void**) C ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(C);
*ierr = LMEGetRHS(
	(LME)PetscToPointer((lme) ),C);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! C_null && !*(void**) C) * (void **) C = (void *)-2;
}
SLEPC_EXTERN void  lmesetsolution_(LME lme,Mat X, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
CHKFORTRANNULLOBJECT(X);
*ierr = LMESetSolution(
	(LME)PetscToPointer((lme) ),
	(Mat)PetscToPointer((X) ));
}
SLEPC_EXTERN void  lmegetsolution_(LME lme,Mat *X, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
PetscBool X_null = !*(void**) X ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(X);
*ierr = LMEGetSolution(
	(LME)PetscToPointer((lme) ),X);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! X_null && !*(void**) X) * (void **) X = (void *)-2;
}
SLEPC_EXTERN void  lmeallocatesolution_(LME lme,PetscInt *extra, int *ierr)
{
CHKFORTRANNULLOBJECT(lme);
*ierr = LMEAllocateSolution(
	(LME)PetscToPointer((lme) ),*extra);
}
#if defined(__cplusplus)
}
#endif

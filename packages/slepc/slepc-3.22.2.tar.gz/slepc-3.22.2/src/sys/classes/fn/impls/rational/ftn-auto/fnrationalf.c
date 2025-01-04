#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* fnrational.c */
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

#include "slepcfn.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnrationalsetnumerator_ FNRATIONALSETNUMERATOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnrationalsetnumerator_ fnrationalsetnumerator
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnrationalsetdenominator_ FNRATIONALSETDENOMINATOR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnrationalsetdenominator_ fnrationalsetdenominator
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  fnrationalsetnumerator_(FN fn,PetscInt *np,PetscScalar pcoeff[], int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLSCALAR(pcoeff);
*ierr = FNRationalSetNumerator(
	(FN)PetscToPointer((fn) ),*np,pcoeff);
}
SLEPC_EXTERN void  fnrationalsetdenominator_(FN fn,PetscInt *nq,PetscScalar qcoeff[], int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLSCALAR(qcoeff);
*ierr = FNRationalSetDenominator(
	(FN)PetscToPointer((fn) ),*nq,qcoeff);
}
#if defined(__cplusplus)
}
#endif

#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* interpol.c */
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

#include "slepcnep.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepinterpolsetinterpolation_ NEPINTERPOLSETINTERPOLATION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepinterpolsetinterpolation_ nepinterpolsetinterpolation
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepinterpolgetinterpolation_ NEPINTERPOLGETINTERPOLATION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepinterpolgetinterpolation_ nepinterpolgetinterpolation
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepinterpolsetpep_ NEPINTERPOLSETPEP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepinterpolsetpep_ nepinterpolsetpep
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepinterpolgetpep_ NEPINTERPOLGETPEP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepinterpolgetpep_ nepinterpolgetpep
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepinterpolsetinterpolation_(NEP nep,PetscReal *tol,PetscInt *deg, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPInterpolSetInterpolation(
	(NEP)PetscToPointer((nep) ),*tol,*deg);
}
SLEPC_EXTERN void  nepinterpolgetinterpolation_(NEP nep,PetscReal *tol,PetscInt *deg, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLREAL(tol);
CHKFORTRANNULLINTEGER(deg);
*ierr = NEPInterpolGetInterpolation(
	(NEP)PetscToPointer((nep) ),tol,deg);
}
SLEPC_EXTERN void  nepinterpolsetpep_(NEP nep,PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
CHKFORTRANNULLOBJECT(pep);
*ierr = NEPInterpolSetPEP(
	(NEP)PetscToPointer((nep) ),
	(PEP)PetscToPointer((pep) ));
}
SLEPC_EXTERN void  nepinterpolgetpep_(NEP nep,PEP *pep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool pep_null = !*(void**) pep ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(pep);
*ierr = NEPInterpolGetPEP(
	(NEP)PetscToPointer((nep) ),pep);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! pep_null && !*(void**) pep) * (void **) pep = (void *)-2;
}
#if defined(__cplusplus)
}
#endif

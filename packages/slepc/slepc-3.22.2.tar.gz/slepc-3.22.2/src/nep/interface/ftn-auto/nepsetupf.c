#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* nepsetup.c */
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
#define nepsetdstype_ NEPSETDSTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetdstype_ nepsetdstype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetup_ NEPSETUP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetup_ nepsetup
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepsetinitialspace_ NEPSETINITIALSPACE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepsetinitialspace_ nepsetinitialspace
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define nepallocatesolution_ NEPALLOCATESOLUTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define nepallocatesolution_ nepallocatesolution
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  nepsetdstype_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetDSType(
	(NEP)PetscToPointer((nep) ));
}
SLEPC_EXTERN void  nepsetup_(NEP nep, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPSetUp(
	(NEP)PetscToPointer((nep) ));
}
SLEPC_EXTERN void  nepsetinitialspace_(NEP nep,PetscInt *n,Vec is[], int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
PetscBool is_null = !*(void**) is ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(is);
*ierr = NEPSetInitialSpace(
	(NEP)PetscToPointer((nep) ),*n,is);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! is_null && !*(void**) is) * (void **) is = (void *)-2;
}
SLEPC_EXTERN void  nepallocatesolution_(NEP nep,PetscInt *extra, int *ierr)
{
CHKFORTRANNULLOBJECT(nep);
*ierr = NEPAllocateSolution(
	(NEP)PetscToPointer((nep) ),*extra);
}
#if defined(__cplusplus)
}
#endif

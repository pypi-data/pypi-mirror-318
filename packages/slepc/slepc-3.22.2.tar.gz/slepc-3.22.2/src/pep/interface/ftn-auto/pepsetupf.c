#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* pepsetup.c */
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
#define pepsetdstype_ PEPSETDSTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetdstype_ pepsetdstype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetup_ PEPSETUP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetup_ pepsetup
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetoperators_ PEPSETOPERATORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetoperators_ pepsetoperators
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetoperators_ PEPGETOPERATORS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetoperators_ pepgetoperators
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepgetnummatrices_ PEPGETNUMMATRICES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepgetnummatrices_ pepgetnummatrices
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepsetinitialspace_ PEPSETINITIALSPACE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepsetinitialspace_ pepsetinitialspace
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define pepallocatesolution_ PEPALLOCATESOLUTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define pepallocatesolution_ pepallocatesolution
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  pepsetdstype_(PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetDSType(
	(PEP)PetscToPointer((pep) ));
}
SLEPC_EXTERN void  pepsetup_(PEP pep, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPSetUp(
	(PEP)PetscToPointer((pep) ));
}
SLEPC_EXTERN void  pepsetoperators_(PEP pep,PetscInt *nmat,Mat A[], int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = PEPSetOperators(
	(PEP)PetscToPointer((pep) ),*nmat,A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  pepgetoperators_(PEP pep,PetscInt *k,Mat *A, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = PEPGetOperators(
	(PEP)PetscToPointer((pep) ),*k,A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  pepgetnummatrices_(PEP pep,PetscInt *nmat, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
CHKFORTRANNULLINTEGER(nmat);
*ierr = PEPGetNumMatrices(
	(PEP)PetscToPointer((pep) ),nmat);
}
SLEPC_EXTERN void  pepsetinitialspace_(PEP pep,PetscInt *n,Vec is[], int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
PetscBool is_null = !*(void**) is ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(is);
*ierr = PEPSetInitialSpace(
	(PEP)PetscToPointer((pep) ),*n,is);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! is_null && !*(void**) is) * (void **) is = (void *)-2;
}
SLEPC_EXTERN void  pepallocatesolution_(PEP pep,PetscInt *extra, int *ierr)
{
CHKFORTRANNULLOBJECT(pep);
*ierr = PEPAllocateSolution(
	(PEP)PetscToPointer((pep) ),*extra);
}
#if defined(__cplusplus)
}
#endif
